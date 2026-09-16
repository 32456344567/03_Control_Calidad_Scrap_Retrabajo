import os
import sys
import threading
import duckdb
import pandas as pd
import numpy as np
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="Executive Quality Control & COPQ Analytics Platform",
    description="Tablero Ejecutivo de Aseguramiento de Calidad, Scrap y Cost of Poor Quality",
    version="2.0.0"
)

# Concurrencia segura para DuckDB
db_lock = threading.Lock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "powerbi_calidad_copq.csv")

# Inicializar base de datos DuckDB en memoria
duck_conn = duckdb.connect(database=":memory:")

def init_database():
    with db_lock:
        if os.path.exists(DATA_PATH):
            df = pd.read_csv(DATA_PATH, encoding="utf-8")
            duck_conn.execute("CREATE OR REPLACE TABLE quality_events AS SELECT * FROM df")
            print(f"DuckDB cargado exitosamente: {len(df):,} registros.")
        else:
            print(f"ADVERTENCIA: Archivo no encontrado en {DATA_PATH}")

init_database()

def build_where_clause(plant: str = "all", line: str = "all", shift: str = "all") -> str:
    clauses = []
    if plant and plant != "all":
        clauses.append(f"plant = '{plant}'")
    if line and line != "all":
        clauses.append(f"line = '{line}'")
    if shift and shift != "all":
        clauses.append(f"shift = '{shift}'")
    
    if clauses:
        return "WHERE " + " AND ".join(clauses)
    return ""

@app.get("/api/health")
def health_check():
    with db_lock:
        count = duck_conn.execute("SELECT COUNT(*) FROM quality_events").fetchone()[0]
    return {
        "status": "online",
        "system": "QA/QC COPQ Industrial Dashboard",
        "dataset_records": count,
        "author": "Angelo Apolo"
    }

@app.get("/api/filters")
def get_filters():
    with db_lock:
        plants = [r[0] for r in duck_conn.execute("SELECT DISTINCT plant FROM quality_events WHERE plant IS NOT NULL ORDER BY plant").fetchall()]
        lines = [r[0] for r in duck_conn.execute("SELECT DISTINCT line FROM quality_events WHERE line IS NOT NULL ORDER BY line").fetchall()]
        shifts = [r[0] for r in duck_conn.execute("SELECT DISTINCT shift FROM quality_events WHERE shift IS NOT NULL ORDER BY shift").fetchall()]
    return {
        "plants": ["all"] + plants,
        "lines": ["all"] + lines,
        "shifts": ["all"] + shifts
    }

@app.get("/api/dashboard")
def get_dashboard_data(
    plant: str = Query("all"),
    line: str = Query("all"),
    shift: str = Query("all")
):
    where_sql = build_where_clause(plant, line, shift)
    
    with db_lock:
        # 1. Resumen General / KPIs
        kpi_query = f"""
            SELECT
                COUNT(*) AS total_records,
                COALESCE(SUM(CASE WHEN categoria_copq != 'Costo Operativo Estándar' THEN cost_usd ELSE 0 END), 0) AS copq_total,
                COALESCE(SUM(scrap), 0) AS scrap_units,
                COALESCE(SUM(decision_rework), 0) AS rework_units,
                COALESCE(SUM(CASE WHEN desenlace_operativo = 'Retrabajo Exitoso' THEN 1 ELSE 0 END), 0) AS rework_success_units,
                COALESCE(SUM(CASE WHEN desenlace_operativo = 'Retrabajo Fallido (Scrap)' THEN 1 ELSE 0 END), 0) AS rework_failed_units,
                COALESCE(SUM(costo_perdida_doble), 0) AS failed_rework_loss,
                COALESCE(SUM(warranty_claim_90d), 0) AS warranty_claims
            FROM quality_events
            {where_sql}
        """
        kpi_res = duck_conn.execute(kpi_query).fetchone()
        
        total_rec = kpi_res[0] or 1
        copq_total = float(kpi_res[1] or 0.0)
        scrap_units = int(kpi_res[2] or 0)
        rework_units = int(kpi_res[3] or 0)
        rework_success = int(kpi_res[4] or 0)
        rework_failed = int(kpi_res[5] or 0)
        failed_rework_loss = float(kpi_res[6] or 0.0)
        warranty_claims = int(kpi_res[7] or 0)
        
        scrap_rate = round((scrap_units / total_rec) * 100, 2)
        rework_rate = round((rework_units / total_rec) * 100, 2)
        rework_success_rate = round((rework_success / rework_units * 100), 1) if rework_units > 0 else 0.0
        warranty_escape_rate = round((warranty_claims / total_rec) * 100, 2)
        annual_savings = round(failed_rework_loss * 10, 2)
        
        summary_kpis = {
            "total_records": total_rec,
            "copq_total": copq_total,
            "copq_total_formatted": f"${copq_total:,.2f}",
            "scrap_units": scrap_units,
            "scrap_rate": scrap_rate,
            "scrap_rate_formatted": f"{scrap_rate:.2f}%",
            "rework_units": rework_units,
            "rework_rate": rework_rate,
            "rework_rate_formatted": f"{rework_rate:.2f}%",
            "rework_success_units": rework_success,
            "rework_success_rate": rework_success_rate,
            "rework_success_rate_formatted": f"{rework_success_rate:.1f}%",
            "rework_failed_units": rework_failed,
            "failed_rework_loss": failed_rework_loss,
            "failed_rework_loss_formatted": f"${failed_rework_loss:,.2f}",
            "annual_savings_projected": annual_savings,
            "annual_savings_formatted": f"+${annual_savings:,.0f} USD",
            "warranty_claims": warranty_claims,
            "warranty_escape_rate": warranty_escape_rate,
            "warranty_escape_rate_formatted": f"{warranty_escape_rate:.2f}%"
        }
        
        # 2. Página 1: Costo Medio por Desenlace Operativo
        q_outcomes = f"""
            SELECT 
                desenlace_operativo,
                ROUND(AVG(cost_usd), 2) AS costo_medio,
                COUNT(*) AS conteo
            FROM quality_events
            {where_sql}
            GROUP BY desenlace_operativo
            ORDER BY costo_medio ASC
        """
        df_outcomes = duck_conn.execute(q_outcomes).df()
        
        color_outcome_map = {
            "Aprobado Directo": "#2ECC71",
            "Rechazado Sin Scrap": "#94A3B8",
            "Retrabajo Exitoso": "#3498DB",
            "Retrabajo No Conforme": "#F59E0B",
            "Scrap Directo": "#E67E22",
            "Retrabajo Fallido (Scrap)": "#C0392B"
        }
        
        cost_by_outcome = []
        for _, row in df_outcomes.iterrows():
            d_name = str(row["desenlace_operativo"])
            cost_by_outcome.append({
                "desenlace": d_name,
                "costo_medio": float(row["costo_medio"]),
                "conteo": int(row["conteo"]),
                "color": color_outcome_map.get(d_name, "#64748B")
            })
            
        # 3. Página 1: Desglose COPQ por Categoría
        q_copq = f"""
            SELECT 
                categoria_copq,
                ROUND(SUM(cost_usd), 2) AS total_usd,
                COUNT(*) AS conteo
            FROM quality_events
            {where_sql}
            {"AND" if where_sql else "WHERE"} categoria_copq != 'Costo Operativo Estándar'
            GROUP BY categoria_copq
            ORDER BY total_usd DESC
        """
        df_copq = duck_conn.execute(q_copq).df()
        copq_sum = df_copq["total_usd"].sum() if not df_copq.empty else 1.0
        
        color_copq_map = {
            "Falla Interna (Retrabajo)": "#3498DB",
            "Falla Interna (Scrap)": "#E67E22",
            "Falla Externa (Reclamo Garantía)": "#C0392B"
        }
        
        copq_breakdown = []
        for _, row in df_copq.iterrows():
            c_name = str(row["categoria_copq"])
            tot = float(row["total_usd"])
            copq_breakdown.append({
                "categoria": c_name,
                "total_usd": tot,
                "pct": round((tot / copq_sum) * 100, 1),
                "conteo": int(row["conteo"]),
                "color": color_copq_map.get(c_name, "#64748B")
            })
            
        # 4. Página 2: Pareto de Defectos (Costo y Frecuencia)
        q_pareto = f"""
            SELECT 
                defect_type,
                ROUND(SUM(cost_usd), 2) AS total_costo,
                COUNT(*) AS frecuencia
            FROM quality_events
            {where_sql}
            {"AND" if where_sql else "WHERE"} defect_type != 'none'
            GROUP BY defect_type
            ORDER BY total_costo DESC
        """
        df_pareto = duck_conn.execute(q_pareto).df()
        
        defect_label_map = {
            "dimension": "Dimensión",
            "finish": "Acabado",
            "contamination": "Contaminación",
            "crack": "Grieta",
            "scratch": "Rayadura"
        }
        
        pareto_data = {
            "labels": [],
            "costs": [],
            "counts": [],
            "cumulative_pct": []
        }
        
        total_p_cost = df_pareto["total_costo"].sum() if not df_pareto.empty else 1.0
        cum = 0.0
        for _, row in df_pareto.iterrows():
            d_raw = str(row["defect_type"])
            c_val = float(row["total_costo"])
            cnt = int(row["frecuencia"])
            cum += c_val
            
            pareto_data["labels"].append(defect_label_map.get(d_raw, d_raw.capitalize()))
            pareto_data["costs"].append(c_val)
            pareto_data["counts"].append(cnt)
            pareto_data["cumulative_pct"].append(round((cum / total_p_cost) * 100, 1))
            
        # 5. Página 2: Tasa de Defectos por Rango de Velocidad
        q_speed = f"""
            SELECT 
                rango_velocidad,
                ROUND(AVG(CASE WHEN defect_severity_0to3 > 0 THEN 100.0 ELSE 0.0 END), 2) AS defect_rate,
                COUNT(*) AS total_lotes
            FROM quality_events
            {where_sql}
            GROUP BY rango_velocidad
        """
        df_speed = duck_conn.execute(q_speed).df()
        
        speed_order = ["Baja (<105 u/h)", "Nominal (105-121 u/h)", "Alta (121-139 u/h)", "Forzada (>139 u/h)"]
        speed_data = {"categories": [], "rates": [], "counts": [], "colors": []}
        speed_color_map = {
            "Baja (<105 u/h)": "#10B981",
            "Nominal (105-121 u/h)": "#3B82F6",
            "Alta (121-139 u/h)": "#F59E0B",
            "Forzada (>139 u/h)": "#EF4444"
        }
        
        speed_dict = {row["rango_velocidad"]: row for _, row in df_speed.iterrows()}
        for s_cat in speed_order:
            if s_cat in speed_dict:
                row = speed_dict[s_cat]
                speed_data["categories"].append(s_cat)
                speed_data["rates"].append(float(row["defect_rate"]))
                speed_data["counts"].append(int(row["total_lotes"]))
                speed_data["colors"].append(speed_color_map.get(s_cat, "#3B82F6"))
                
        # 6. Página 2: Degradación por Antigüedad de Máquina
        q_age = f"""
            SELECT 
                rango_antiguedad,
                ROUND(AVG(CASE WHEN defect_severity_0to3 > 0 THEN 100.0 ELSE 0.0 END), 2) AS defect_rate,
                COUNT(*) AS total_lotes
            FROM quality_events
            {where_sql}
            GROUP BY rango_antiguedad
        """
        df_age = duck_conn.execute(q_age).df()
        age_order = ["Nueva (<4 años)", "Estable (4-6 años)", "Intermedia (6-8 años)", "Desgaste Crítico (>8 años)"]
        age_data = {"categories": [], "rates": [], "counts": [], "colors": []}
        age_color_map = {
            "Nueva (<4 años)": "#10B981",
            "Estable (4-6 años)": "#3B82F6",
            "Intermedia (6-8 años)": "#F59E0B",
            "Desgaste Crítico (>8 años)": "#EF4444"
        }
        age_dict = {row["rango_antiguedad"]: row for _, row in df_age.iterrows()}
        for a_cat in age_order:
            if a_cat in age_dict:
                row = age_dict[a_cat]
                age_data["categories"].append(a_cat)
                age_data["rates"].append(float(row["defect_rate"]))
                age_data["counts"].append(int(row["total_lotes"]))
                age_data["colors"].append(age_color_map.get(a_cat, "#3B82F6"))
                
        # 7. Página 3: Escape a Garantía por Método de Inspección
        q_inspection = f"""
            SELECT 
                inspection_method,
                ROUND(AVG(warranty_claim_90d) * 100, 2) AS escape_rate,
                SUM(warranty_claim_90d) AS reclamos,
                COUNT(*) AS inspeccionados
            FROM quality_events
            {where_sql}
            GROUP BY inspection_method
            ORDER BY escape_rate ASC
        """
        df_insp = duck_conn.execute(q_inspection).df()
        insp_name_map = {
            "sensor": "Sensores Inteligentes",
            "vision": "Visión Artificial",
            "manual": "Inspección Manual"
        }
        insp_color_map = {
            "sensor": "#10B981",
            "vision": "#3B82F6",
            "manual": "#F59E0B"
        }
        
        inspection_data = {"categories": [], "rates": [], "claims": [], "totals": [], "colors": []}
        for _, row in df_insp.iterrows():
            m_raw = str(row["inspection_method"])
            inspection_data["categories"].append(insp_name_map.get(m_raw, m_raw.capitalize()))
            inspection_data["rates"].append(float(row["escape_rate"]))
            inspection_data["claims"].append(int(row["reclamos"]))
            inspection_data["totals"].append(int(row["inspeccionados"]))
            inspection_data["colors"].append(insp_color_map.get(m_raw, "#64748B"))
            
        # 8. Página 3: Reclamos por Grado de Materia Prima
        q_material = f"""
            SELECT 
                material_grade,
                COUNT(*) AS reclamos
            FROM quality_events
            {where_sql}
            {"AND" if where_sql else "WHERE"} warranty_claim_90d = 1
            GROUP BY material_grade
            ORDER BY reclamos DESC
        """
        df_mat = duck_conn.execute(q_material).df()
        mat_name_map = {
            "grade_A": "Grado A (Premium)",
            "grade_B": "Grado B (Estándar)",
            "grade_C": "Grado C (Económico)"
        }
        mat_color_map = {
            "grade_A": "#3B82F6",
            "grade_B": "#8B5CF6",
            "grade_C": "#F59E0B"
        }
        
        material_data = {"labels": [], "series": [], "colors": []}
        for _, row in df_mat.iterrows():
            g_raw = str(row["material_grade"])
            material_data["labels"].append(mat_name_map.get(g_raw, g_raw.capitalize()))
            material_data["series"].append(int(row["reclamos"]))
            material_data["colors"].append(mat_color_map.get(g_raw, "#3B82F6"))
            
        # 9. Registros Críticos Recientes
        q_recent = f"""
            SELECT 
                event_id,
                plant,
                line,
                shift,
                defect_type,
                defect_severity_0to3,
                decision_rework,
                desenlace_operativo,
                cost_usd,
                costo_perdida_doble,
                warranty_claim_90d
            FROM quality_events
            {where_sql}
            ORDER BY defect_severity_0to3 DESC, cost_usd DESC
            LIMIT 25
        """
        df_recent = duck_conn.execute(q_recent).df()
        recent_events = df_recent.to_dict(orient="records")

    return {
        "summary_kpis": summary_kpis,
        "page1_charts": {
            "cost_by_outcome": cost_by_outcome,
            "copq_breakdown": copq_breakdown
        },
        "page2_charts": {
            "pareto": pareto_data,
            "defects_by_speed": speed_data,
            "defects_by_age": age_data
        },
        "page3_charts": {
            "escape_by_inspection": inspection_data,
            "claims_by_material": material_data
        },
        "recent_events": recent_events
    }

@app.get("/api/events")
def get_events_paginated(
    plant: str = "all",
    line: str = "all",
    shift: str = "all",
    severity: str = "all",
    search: str = "",
    limit: int = 25,
    offset: int = 0
):
    where_sql = build_where_clause(plant, line, shift)
    extra_clauses = []
    
    if severity != "all" and severity.isdigit():
        extra_clauses.append(f"defect_severity_0to3 = {int(severity)}")
        
    if search:
        s = search.replace("'", "''").lower()
        extra_clauses.append(f"(LOWER(event_id) LIKE '%{s}%' OR LOWER(defect_type) LIKE '%{s}%' OR LOWER(desenlace_operativo) LIKE '%{s}%')")
        
    if extra_clauses:
        if where_sql:
            where_sql += " AND " + " AND ".join(extra_clauses)
        else:
            where_sql = "WHERE " + " AND ".join(extra_clauses)
            
    with db_lock:
        tot_count = duck_conn.execute(f"SELECT COUNT(*) FROM quality_events {where_sql}").fetchone()[0]
        q_page = f"""
            SELECT 
                event_id,
                plant,
                line,
                shift,
                defect_type,
                defect_severity_0to3,
                decision_rework,
                desenlace_operativo,
                cost_usd,
                costo_perdida_doble,
                warranty_claim_90d
            FROM quality_events
            {where_sql}
            ORDER BY defect_severity_0to3 DESC, cost_usd DESC
            LIMIT {limit} OFFSET {offset}
        """
        rows = duck_conn.execute(q_page).df().to_dict(orient="records")
        
    return {
        "total": tot_count,
        "limit": limit,
        "offset": offset,
        "items": rows
    }

@app.get("/", response_class=HTMLResponse)
def serve_dashboard():
    tmpl_path = os.path.join(BASE_DIR, "templates", "index.html")
    if os.path.exists(tmpl_path):
        with open(tmpl_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h2>Error: templates/index.html no encontrado.</h2>", status_code=404)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8503))
    is_dev = os.environ.get("RELOAD", "false").lower() == "true"
    print(f"Iniciando Executive Quality Dashboard en http://localhost:{port}")
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=is_dev)