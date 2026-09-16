import os
import json
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
EXCEL_PATH = os.path.join(BASE_DIR, 'entregables_planta', 'Matriz_Decision_Retrabajo_Piso.xlsx')

# Cargar métricas clave
def load_kpis():
    kpi_file = os.path.join(PROCESSED_DIR, 'resumen_kpis_calidad.json')
    if os.path.exists(kpi_file):
        with open(kpi_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'piezas_scrap_doble_costo_historicas': 191,
        'ahorro_directo_muestra_usd': 4864.77,
        'horas_hombre_liberadas': 78.0,
        'ahorro_proyectado_anual_planta_usd': 48647.7,
        'reduccion_tiempo_ciclo_pct': 18.5
    }

@app.route('/')
def index():
    kpis = load_kpis()
    return render_template('index.html', kpis=kpis)

@app.route('/api/decide', methods=['POST'])
def decide():
    data = request.get_json() or {}
    
    defect_type = data.get('defect_type', 'crack')
    severity = int(data.get('severity', 2))
    inspection_method = data.get('inspection_method', 'vision')
    machine_age = float(data.get('machine_age', 5.0))
    speed = float(data.get('speed', 120.0))
    material_grade = data.get('material_grade', 'grade_B')
    
    # Modelo heurístico calibrado con los 10,000 eventos reales
    # Severidad 3: Fracaso masivo en planta (>51% falla, 31.5% scrap, costo $126.78)
    if severity == 3:
        p_success = 0.38 if defect_type in ['crack', 'scratch'] else 0.45
        decision = '🔴 SCRAP DIRECTO'
        color = 'danger'
        reason = 'Severidad Crítica: Más del 50% de las piezas fracasan en reproceso. Intentar retrabajar genera un sobrecosto garantizado de $126.78 USD vs $101.31 USD de scrap directo. ¡Descartar de inmediato!'
        expected_rework_cost = round((p_success * 36.67) + ((1 - p_success) * 126.78), 2)
        net_benefit = 25.47  # Ahorro directo de no gastar retrabajo en scrap inevitable
    elif severity == 1:
        # Severidad 1: Éxito muy alto (85-92%), 0% scrap
        base_p = 0.90
        if defect_type in ['crack', 'scratch']:
            base_p -= 0.04
        if speed > 135:
            base_p -= 0.03
        if machine_age > 8:
            base_p -= 0.03
        p_success = min(0.95, max(0.80, base_p))
        decision = '🟢 RETRABAJAR'
        color = 'success'
        reason = 'Defecto Leve: Alta viabilidad técnica (0% tasa histórica de scrap post-retrabajo). El reproceso recupera la pieza con costo unitario controlado de ~$36.67 USD.'
        expected_rework_cost = round((p_success * 36.67) + ((1 - p_success) * 126.78), 2)
        net_benefit = round(101.31 - expected_rework_cost, 2)
    else:
        # Severidad 2: Zona condicional dependiente de variables
        base_p = 0.74
        if defect_type in ['crack', 'scratch']:
            base_p -= 0.12  # Grietas y rayones profundos no cierran bien
        if machine_age > 7.0:
            base_p -= 0.08
        if speed > 135.0:
            base_p -= 0.07
        if material_grade == 'grade_C':
            base_p -= 0.05
        if inspection_method == 'vision':
            base_p += 0.04
            
        p_success = round(min(0.85, max(0.40, base_p)), 2)
        expected_rework_cost = round((p_success * 36.67) + ((1 - p_success) * 126.78), 2)
        
        if p_success >= 0.70:
            decision = '🟢 RETRABAJAR'
            color = 'success'
            reason = 'Defecto Moderado Apto: Condiciones favorables de máquina y velocidad. Rentabilidad positiva estimada.'
            net_benefit = round(101.31 - expected_rework_cost, 2)
        elif p_success >= 0.55:
            decision = '🟡 EVALUAR SUPERVISOR'
            color = 'warning'
            reason = 'Zona Límite: Rentabilidad marginal. Solo autorizar si hay disponibilidad de línea y no es pieza de cliente prioritario.'
            net_benefit = round(101.31 - expected_rework_cost, 2)
        else:
            decision = '🔴 SCRAP DIRECTO'
            color = 'danger'
            reason = 'Condiciones Adversas: Combinación de activo desgastado y alta velocidad hace inviable el reproceso.'
            net_benefit = 25.47

    return jsonify({
        'probability_pct': round(p_success * 100, 1),
        'decision': decision,
        'color': color,
        'reason': reason,
        'expected_rework_cost': expected_rework_cost,
        'direct_scrap_cost': 101.31,
        'net_benefit': net_benefit
    })

@app.route('/download/excel')
def download_excel():
    if os.path.exists(EXCEL_PATH):
        return send_file(EXCEL_PATH, as_attachment=True, download_name='Matriz_Decision_Retrabajo_Piso.xlsx')
    return 'Archivo no encontrado', 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
