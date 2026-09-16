import json
import os

csv_path = r"C:\Users\apolo\Mi unidad\Estrategias para conseguir un mejor empleo\proyectos_portafolio\03_Control_Calidad_Scrap_Retrabajo\data\processed\powerbi_calidad_copq.csv"
csv_path_escaped = csv_path.replace("\\", "\\\\")

m_expr = f'''let
    Source = Csv.Document(File.Contents("{csv_path_escaped}"),[Delimiter=",", Columns=29, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{
        {{"event_id", type text}}, {{"event_ts", type datetime}}, {{"plant", type text}}, {{"line", type text}},
        {{"shift", type text}}, {{"machine_id", type text}}, {{"operator_id", type text}}, {{"machine_age_yrs", type number}},
        {{"material_grade", type text}}, {{"temp_c", type number}}, {{"humidity_pct", type number}},
        {{"process_speed_units_hr", type number}}, {{"inspection_method", type text}}, {{"defect_type", type text}},
        {{"defect_severity_0to3", Int64.Type}}, {{"decision_rework", Int64.Type}}, {{"rework_time_min", type number}},
        {{"final_pass", Int64.Type}}, {{"scrap", Int64.Type}}, {{"total_cycle_time_min", type number}},
        {{"energy_kwh", type number}}, {{"cost_usd", type number}}, {{"warranty_claim_90d", Int64.Type}},
        {{"categoria_copq", type text}}, {{"desenlace_operativo", type text}}, {{"costo_perdida_doble", type number}},
        {{"rango_velocidad", type text}}, {{"rango_antiguedad", type text}}, {{"severidad_label", type text}}
    }}, "en-US")
in
    #"Changed Type"'''

bim_paths = [
    'powerbi/model.bim',
    'powerbi/Calidad_COPQ.SemanticModel/model.bim'
]

for p in bim_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        data['model']['tables'][0]['partitions'][0]['source']['expression'] = m_expr
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print('[OK] Updated BIM:', p)

tmdl_path = 'powerbi/Calidad_COPQ.SemanticModel/definition/tables/FactCalidad.tmdl'
if os.path.exists(tmdl_path):
    with open(tmdl_path, 'r', encoding='utf-8') as f:
        content = f.read()
    split_idx = content.find('partition FactCalidad = m')
    if split_idx != -1:
        before = content[:split_idx]
        tmdl_m = f'''partition FactCalidad = m
		mode: import
		source =
			let
			    Source = Csv.Document(File.Contents("{csv_path_escaped}"),[Delimiter=",", Columns=29, Encoding=65001, QuoteStyle=QuoteStyle.None]),
			    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
			    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{
			        {{"event_id", type text}}, {{"event_ts", type datetime}}, {{"plant", type text}}, {{"line", type text}},
			        {{"shift", type text}}, {{"machine_id", type text}}, {{"operator_id", type text}}, {{"machine_age_yrs", type number}},
			        {{"material_grade", type text}}, {{"temp_c", type number}}, {{"humidity_pct", type number}},
			        {{"process_speed_units_hr", type number}}, {{"inspection_method", type text}}, {{"defect_type", type text}},
			        {{"defect_severity_0to3", Int64.Type}}, {{"decision_rework", Int64.Type}}, {{"rework_time_min", type number}},
			        {{"final_pass", Int64.Type}}, {{"scrap", Int64.Type}}, {{"total_cycle_time_min", type number}},
			        {{"energy_kwh", type number}}, {{"cost_usd", type number}}, {{"warranty_claim_90d", Int64.Type}},
			        {{"categoria_copq", type text}}, {{"desenlace_operativo", type text}}, {{"costo_perdida_doble", type number}},
			        {{"rango_velocidad", type text}}, {{"rango_antiguedad", type text}}, {{"severidad_label", type text}}
			    }}, "en-US")
			in
			    #"Changed Type"
'''
        with open(tmdl_path, 'w', encoding='utf-8') as f:
            f.write(before + tmdl_m)
        print('[OK] Updated TMDL:', tmdl_path)
