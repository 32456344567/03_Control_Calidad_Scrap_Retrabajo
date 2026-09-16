import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()

# Sheet 1: Calculadora de Piso
ws1 = wb.active
ws1.title = 'Semaforo_Decision_Piso'
ws1.views.sheetView[0].showGridLines = True

# Paleta corporativa sobria
NAVY_HEADER = '1B365D'
WHITE = 'FFFFFF'
LIGHT_GRAY = 'F2F4F7'
BORDER_GRAY = 'D0D5DD'
GREEN_FILL = 'D1E7DD'
GREEN_TEXT = '0F5132'
YELLOW_FILL = 'FFF3CD'
YELLOW_TEXT = '664D03'
RED_FILL = 'F8D7DA'
RED_TEXT = '842029'

font_title = Font(name='Calibri', size=16, bold=True, color=NAVY_HEADER)
font_subtitle = Font(name='Calibri', size=11, italic=True, color='475467')
font_sec_header = Font(name='Calibri', size=12, bold=True, color=WHITE)
font_label = Font(name='Calibri', size=11, bold=True)
font_val = Font(name='Calibri', size=11)
font_bold = Font(name='Calibri', size=11, bold=True)

fill_sec = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type='solid')
fill_input = PatternFill(start_color='E8F4FD', end_color='E8F4FD', fill_type='solid')
fill_kpi = PatternFill(start_color=LIGHT_GRAY, end_color=LIGHT_GRAY, fill_type='solid')

thin = Side(border_style='thin', color=BORDER_GRAY)
border_cell = Border(top=thin, left=thin, right=thin, bottom=thin)

# Title
ws1.merge_cells('B2:H2')
ws1['B2'] = 'HERRAMIENTA DE DECISIÓN EN PISO: SEMÁFORO RETRABAJO VS. SCRAP'
ws1['B2'].font = font_title
ws1['B2'].alignment = Alignment(vertical='center')

ws1.merge_cells('B3:H3')
ws1['B3'] = 'Aseguramiento de Calidad & Control de Costos (COPQ) | Ing. Angelo Apolo'
ws1['B3'].font = font_subtitle
ws1['B3'].alignment = Alignment(vertical='center')

# Section 1: Inputs
ws1.merge_cells('B5:D5')
ws1['B5'] = '1. PARÁMETROS DE INSPECCIÓN EN LÍNEA'
ws1['B5'].font = font_sec_header
ws1['B5'].fill = fill_sec
ws1['B5'].alignment = Alignment(horizontal='center', vertical='center')

inputs = [
    ('Tipo de Defecto:', 'Grieta / Fisura', 'B6', 'C6', 'D6'),
    ('Severidad del Defecto (1 a 3):', 2, 'B7', 'C7', 'D7'),
    ('Método de Inspección:', 'Visión Artificial', 'B8', 'C8', 'D8'),
    ('Antigüedad de Máquina (años):', 5.0, 'B9', 'C9', 'D9'),
    ('Velocidad de Operación (u/h):', 125, 'B10', 'C10', 'D10'),
    ('Grado de Materia Prima:', 'Grado B', 'B11', 'C11', 'D11'),
]

for label, default_val, c_lbl, c_val, c_note in inputs:
    ws1[c_lbl] = label
    ws1[c_lbl].font = font_label
    ws1[c_lbl].border = border_cell
    
    ws1[c_val] = default_val
    ws1[c_val].font = font_bold
    ws1[c_val].fill = fill_input
    ws1[c_val].alignment = Alignment(horizontal='center', vertical='center')
    ws1[c_val].border = border_cell

ws1['D6'] = 'Opciones: Dimensión / Acabado / Grieta / Rayón / Contaminación'
ws1['D7'] = '1 = Leve | 2 = Moderado | 3 = Crítico/Estructural'
ws1['D8'] = 'Manual / Sensor / Visión Artificial'
ws1['D9'] = 'Promedio planta: 6.0 años'
ws1['D10'] = 'Nominal: 115 u/h (Forzada: >135 u/h)'
ws1['D11'] = 'Grado A (Premium) / Grado B / Grado C'

for row in range(6, 12):
    ws1[f'D{row}'].font = Font(name='Calibri', size=9, italic=True, color='667085')
    ws1[f'D{row}'].alignment = Alignment(vertical='center')

# Section 2: Output / Semáforo
ws1.merge_cells('F5:H5')
ws1['F5'] = '2. RECOMENDACIÓN OPERATIVA (SEMÁFORO)'
ws1['F5'].font = font_sec_header
ws1['F5'].fill = fill_sec
ws1['F5'].alignment = Alignment(horizontal='center', vertical='center')

# Formula for Prob Exito
ws1['F6'] = 'Probabilidad Estimada de Éxito:'
ws1['F6'].font = font_label
ws1['F6'].border = border_cell

ws1['G6'] = '=MAX(0.05, MIN(0.98, 1.15 - (C7*0.24) - (C9*0.012) - ((C10-100)*0.0015) + IF(C8="Visión Artificial", 0.05, IF(C8="Sensor", 0.02, 0))))'
ws1['G6'].number_format = '0.0%'
ws1['G6'].font = Font(name='Calibri', size=12, bold=True)
ws1['G6'].alignment = Alignment(horizontal='center', vertical='center')
ws1['G6'].border = border_cell

ws1.merge_cells('F7:F8')
ws1['F7'] = 'DICTAMEN EN PISO:'
ws1['F7'].font = Font(name='Calibri', size=12, bold=True)
ws1['F7'].alignment = Alignment(horizontal='center', vertical='center')
ws1['F7'].border = border_cell
ws1['F8'].border = border_cell

ws1.merge_cells('G7:H8')
ws1['G7'] = '=IF(C7=3, "🔴 SCRAP DIRECTO", IF(G6>=0.75, "🟢 RETRABAJAR", IF(G6>=0.55, "🟡 EVALUAR SUPERVISOR", "🔴 SCRAP DIRECTO")))'
ws1['G7'].font = Font(name='Calibri', size=14, bold=True)
ws1['G7'].alignment = Alignment(horizontal='center', vertical='center')
ws1['G7'].border = border_cell

# Cost indicators
ws1['F9'] = 'Costo Esperado si se Retrabaja:'
ws1['F9'].font = font_label
ws1['F9'].border = border_cell
ws1['G9'] = '=(G6*36.67) + ((1-G6)*126.78)'
ws1['G9'].number_format = '$#,##0.00'
ws1['G9'].font = font_bold
ws1['G9'].alignment = Alignment(horizontal='center')
ws1['G9'].border = border_cell

ws1['F10'] = 'Costo si se envía a Scrap Directo:'
ws1['F10'].font = font_label
ws1['F10'].border = border_cell
ws1['G10'] = 101.31
ws1['G10'].number_format = '$#,##0.00'
ws1['G10'].font = font_bold
ws1['G10'].alignment = Alignment(horizontal='center')
ws1['G10'].border = border_cell

ws1['F11'] = 'Beneficio Neto de la Decisión:'
ws1['F11'].font = font_label
ws1['F11'].border = border_cell
ws1['G11'] = '=IF(LEFT(G7,1)="🔴", 126.78 - 101.31, 101.31 - G9)'
ws1['G11'].number_format = '+$#,##0.00;-$#,##0.00;$0.00'
ws1['G11'].font = Font(name='Calibri', size=12, bold=True, color='0F5132')
ws1['G11'].alignment = Alignment(horizontal='center')
ws1['G11'].border = border_cell

# Section 3: Matriz Guía de Piso
ws1.merge_cells('B14:H14')
ws1['B14'] = '3. TABLA GUÍA RÁPIDA DE DECISIÓN SEGÚN SEVERIDAD Y DEFECTO'
ws1['B14'].font = font_sec_header
ws1['B14'].fill = fill_sec
ws1['B14'].alignment = Alignment(horizontal='center', vertical='center')

headers_tab = ['Tipo de Defecto', 'Severidad 1 (Leve)', 'Severidad 2 (Moderado)', 'Severidad 3 (Grave/Estructural)', 'Regla Operativa de Planta']
cols_tab = ['B', 'C', 'D', 'E', 'F']
for i, h in enumerate(headers_tab):
    ws1[f'{cols_tab[i]}15'] = h
    ws1[f'{cols_tab[i]}15'].font = Font(name='Calibri', size=10, bold=True, color=WHITE)
    ws1[f'{cols_tab[i]}15'].fill = PatternFill(start_color='34495E', end_color='34495E', fill_type='solid')
    ws1[f'{cols_tab[i]}15'].alignment = Alignment(horizontal='center', vertical='center')
    ws1[f'{cols_tab[i]}15'].border = border_cell
ws1.merge_cells('F15:H15')

mat_data = [
    ('Dimensión / Tolerancia', '🟢 Retrabajar (88% éxito)', '🟢 Retrabajar (76% éxito)', '🔴 Scrap Directo (<48%)', 'Ajuste de mordazas y calibración en línea.'),
    ('Acabado Superficial', '🟢 Retrabajar (87% éxito)', '🟢 Retrabajar (72% éxito)', '🔴 Scrap Directo (<48%)', 'Pulido o reacondicionado térmico permitido.'),
    ('Contaminación', '🟢 Retrabajar (86% éxito)', '🟡 Evaluar (65% éxito)', '🔴 Scrap Directo (<45%)', 'Limpieza solo si no penetra matriz del material.'),
    ('Rayón Profundo', '🟢 Retrabajar (85% éxito)', '🟡 Evaluar (62% éxito)', '🔴 Scrap Directo (<42%)', 'Inspección de guías mecánicas y rodillos.'),
    ('Grieta / Fisura', '🟢 Retrabajar (82% éxito)', '🟡 Evaluar (58% éxito)', '🔴 Scrap Directo (<38%)', 'PÉRDIDA ESTRUCTURAL: Riesgo crítico de escape a cliente.')
]

for r_idx, row_vals in enumerate(mat_data, start=16):
    ws1[f'B{r_idx}'] = row_vals[0]
    ws1[f'B{r_idx}'].font = font_bold
    ws1[f'B{r_idx}'].border = border_cell
    
    ws1[f'C{r_idx}'] = row_vals[1]
    ws1[f'C{r_idx}'].font = font_val
    ws1[f'C{r_idx}'].fill = PatternFill(start_color=GREEN_FILL, end_color=GREEN_FILL, fill_type='solid')
    ws1[f'C{r_idx}'].alignment = Alignment(horizontal='center')
    ws1[f'C{r_idx}'].border = border_cell
    
    ws1[f'D{r_idx}'] = row_vals[2]
    ws1[f'D{r_idx}'].font = font_val
    fill_d = YELLOW_FILL if '🟡' in row_vals[2] else GREEN_FILL
    ws1[f'D{r_idx}'].fill = PatternFill(start_color=fill_d, end_color=fill_d, fill_type='solid')
    ws1[f'D{r_idx}'].alignment = Alignment(horizontal='center')
    ws1[f'D{r_idx}'].border = border_cell
    
    ws1[f'E{r_idx}'] = row_vals[3]
    ws1[f'E{r_idx}'].font = font_bold
    ws1[f'E{r_idx}'].fill = PatternFill(start_color=RED_FILL, end_color=RED_FILL, fill_type='solid')
    ws1[f'E{r_idx}'].alignment = Alignment(horizontal='center')
    ws1[f'E{r_idx}'].border = border_cell
    
    ws1.merge_cells(f'F{r_idx}:H{r_idx}')
    ws1[f'F{r_idx}'] = row_vals[4]
    ws1[f'F{r_idx}'].font = Font(name='Calibri', size=9, italic=True)
    ws1[f'F{r_idx}'].alignment = Alignment(vertical='center')
    ws1[f'F{r_idx}'].border = border_cell
    ws1[f'H{r_idx}'].border = border_cell

# Adjust column widths
col_widths = {'A': 3, 'B': 28, 'C': 26, 'D': 26, 'E': 26, 'F': 22, 'G': 22, 'H': 22}
for col, width in col_widths.items():
    ws1.column_dimensions[col].width = width

wb.save('entregables_planta/Matriz_Decision_Retrabajo_Piso.xlsx')
print('[OK] Matriz Excel guardada exitosamente en entregables_planta/Matriz_Decision_Retrabajo_Piso.xlsx')
