import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ==========================================
# HOJA 1: LECCIÓN DE UN PUNTO (OPL) DE PISO
# ==========================================
ws1 = wb.active
ws1.title = 'OPL_Criterios_Calidad_Piso'
ws1.views.sheetView[0].showGridLines = True

# Paleta corporativa sobria
NAVY_HEADER = '1B365D'
WHITE = 'FFFFFF'
LIGHT_GRAY = 'F8F9FA'
BORDER_GRAY = 'D0D5DD'
GREEN_FILL = 'D1E7DD'
GREEN_TEXT = '0F5132'
YELLOW_FILL = 'FFF3CD'
YELLOW_TEXT = '664D03'
RED_FILL = 'F8D7DA'
RED_TEXT = '842029'

font_title = Font(name='Calibri', size=15, bold=True, color=NAVY_HEADER)
font_subtitle = Font(name='Calibri', size=10, italic=True, color='475467')
font_sec_header = Font(name='Calibri', size=11, bold=True, color=WHITE)
font_col_header = Font(name='Calibri', size=10, bold=True, color=WHITE)
font_label = Font(name='Calibri', size=10, bold=True)
font_val = Font(name='Calibri', size=10)
font_bold = Font(name='Calibri', size=10, bold=True)

fill_sec = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type='solid')
fill_subhdr = PatternFill(start_color='34495E', end_color='34495E', fill_type='solid')
fill_kpi = PatternFill(start_color=LIGHT_GRAY, end_color=LIGHT_GRAY, fill_type='solid')

thin = Side(border_style='thin', color=BORDER_GRAY)
border_cell = Border(top=thin, left=thin, right=thin, bottom=thin)

# Título y encabezado formal
ws1.merge_cells('A2:G2')
ws1['A2'] = 'LECCIÓN DE UN PUNTO (OPL) | ESTÁNDAR VISUAL DE CALIDAD EN PISO'
ws1['A2'].font = font_title
ws1['A2'].alignment = Alignment(vertical='center')

ws1.merge_cells('A3:G3')
ws1['A3'] = 'Código: OPL-CAL-003 | Revisión: 02 | Aprobado: Ing. Angelo Apolo (Jefe QA/QC & Black Belt) | Líneas A & B'
ws1['A3'].font = font_subtitle
ws1['A3'].alignment = Alignment(vertical='center')

# Regla de Oro destacada en Rojo Alerta
ws1.merge_cells('A5:G5')
ws1['A5'] = '⚠️ REGLA DE ORO DE PLANTA: PROHIBIDO RETRABAJAR DEFECTOS EN SEVERIDAD 3 (GRIETAS O DEFORMACIONES CRÍTICAS)'
ws1['A5'].font = Font(name='Calibri', size=11, bold=True, color=RED_TEXT)
ws1['A5'].fill = PatternFill(start_color=RED_FILL, end_color=RED_FILL, fill_type='solid')
ws1['A5'].alignment = Alignment(horizontal='center', vertical='center')

ws1.merge_cells('A6:G6')
ws1['A6'] = 'Más del 50% de las piezas graves fracasan en reproceso. Retrabajar cuesta $126.78 USD vs. $101.31 USD de Scrap directo. ¡Toda pieza severa va a Gaveta Roja!'
ws1['A6'].font = Font(name='Calibri', size=9, italic=True, color=RED_TEXT)
ws1['A6'].alignment = Alignment(horizontal='center', vertical='center')

# Encabezados de la matriz visual
headers_opl = [
    'Tipo de Defecto',
    'Severidad 1 (Leve)\n🟢 GAVETA VERDE: REPROCESO',
    'Severidad 2 (Moderada)\n🟡 GAVETA AMARILLA: EVALUAR',
    'Severidad 3 (Crítica / Estructural)\n🔴 GAVETA ROJA: SCRAP DIRECTO',
    'Criterio Físico / Tolerancia',
    'Acción Inmediata en Línea',
    'Ahorro Evitado'
]

ws1.row_dimensions[8].height = 32
cols_opl = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i, h in enumerate(headers_opl):
    col = cols_opl[i]
    ws1[f'{col}8'] = h
    ws1[f'{col}8'].font = font_col_header
    ws1[f'{col}8'].fill = fill_subhdr
    ws1[f'{col}8'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws1[f'{col}8'].border = border_cell

# Filas de la matriz de defectos
mat_rows = [
    (
        'Grieta / Fisura\n(crack)',
        'Microfisura capilar no pasante (<2 mm).\nÉxito histórico: 82%',
        'Fisura superficial (2 - 5 mm).\nAutorizado solo con máquina <6 años.\nÉxito histórico: 58%',
        'Fisura pasante o ramificada (>5 mm).\nÉxito: <38% (Fracaso garantizado).',
        'Inspección con lupa 10x y líquido penetrante.',
        'Marcar con pintura roja indeleble y depositar en contenedor de Scrap.',
        '+$25.47 USD / pieza'
    ),
    (
        'Desviación Dimensional\n(dimension)',
        'Desvío menor respecto a cota (±0.05 mm).\nÉxito histórico: 88%',
        'Desvío moderado (±0.10 a 0.25 mm).\nRequiere verificación de espesor de pared.\nÉxito histórico: 76%',
        'Desvío crítico (>0.30 mm) o falta de material.\nImposible recuperar tolerancia.',
        'Medición con micrómetro digital / galga pasa-no pasa.',
        'Ajuste de mordazas de máquina y verificación de setpoint.',
        '+$25.47 USD / pieza'
    ),
    (
        'Acabado Superficial\n(finish)',
        'Rebaba menor o marca de enfriamiento.\nÉxito histórico: 87%',
        'Textura irregular o mancha no penetrante.\nAutorizado si no afecta cara de ensamble.\nÉxito histórico: 72%',
        'Porosidad abierta o desgarre térmico.\nDefecto penetra >20% del espesor de pared.',
        'Comparación contra muestra patrón de rugosidad.',
        'Desbarbado manual en banco auxiliar (máximo 10 min).',
        '+$25.47 USD / pieza'
    ),
    (
        'Rayón / Abrasión\n(scratch)',
        'Rayón leve que no traba la uña (<0.05 mm).\nÉxito histórico: 85%',
        'Rayón visible (0.05 - 0.15 mm).\nEvaluar si compromete estanqueidad o sello.\nÉxito histórico: 62%',
        'Surco profundo (>0.20 mm) o daño en junta.\nRiesgo crítico de reclamo a cliente.',
        'Inspección visual bajo luz halógena estandarizada.',
        'Pulido abrasivo solo en caras no funcionales.',
        '+$25.47 USD / pieza'
    ),
    (
        'Contaminación\n(contamination)',
        'Partículas secas de polvo superficial.\nÉxito histórico: 86%',
        'Mancha de lubricante o grasa lavable.\nRequiere desengrase ultrasónico controlado.\nÉxito histórico: 65%',
        'Inclusiones fundidas o viruta metálica incrustada.\nFalla estructural irreparable.',
        'Verificación con hisopado e inspección óptica.',
        'Limpieza neumática en estación de soplado.',
        '+$25.47 USD / pieza'
    )
]

for r_idx, r_data in enumerate(mat_rows, start=9):
    ws1.row_dimensions[r_idx].height = 42
    ws1[f'A{r_idx}'] = r_data[0]
    ws1[f'A{r_idx}'].font = font_bold
    ws1[f'A{r_idx}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws1[f'A{r_idx}'].border = border_cell
    
    ws1[f'B{r_idx}'] = r_data[1]
    ws1[f'B{r_idx}'].font = font_val
    ws1[f'B{r_idx}'].fill = PatternFill(start_color=GREEN_FILL, end_color=GREEN_FILL, fill_type='solid')
    ws1[f'B{r_idx}'].alignment = Alignment(vertical='center', wrap_text=True)
    ws1[f'B{r_idx}'].border = border_cell
    
    ws1[f'C{r_idx}'] = r_data[2]
    ws1[f'C{r_idx}'].font = font_val
    ws1[f'C{r_idx}'].fill = PatternFill(start_color=YELLOW_FILL, end_color=YELLOW_FILL, fill_type='solid')
    ws1[f'C{r_idx}'].alignment = Alignment(vertical='center', wrap_text=True)
    ws1[f'C{r_idx}'].border = border_cell
    
    ws1[f'D{r_idx}'] = r_data[3]
    ws1[f'D{r_idx}'].font = Font(name='Calibri', size=10, bold=True, color=RED_TEXT)
    ws1[f'D{r_idx}'].fill = PatternFill(start_color=RED_FILL, end_color=RED_FILL, fill_type='solid')
    ws1[f'D{r_idx}'].alignment = Alignment(vertical='center', wrap_text=True)
    ws1[f'D{r_idx}'].border = border_cell
    
    ws1[f'E{r_idx}'] = r_data[4]
    ws1[f'E{r_idx}'].font = font_val
    ws1[f'E{r_idx}'].alignment = Alignment(vertical='center', wrap_text=True)
    ws1[f'E{r_idx}'].border = border_cell
    
    ws1[f'F{r_idx}'] = r_data[5]
    ws1[f'F{r_idx}'].font = font_val
    ws1[f'F{r_idx}'].alignment = Alignment(vertical='center', wrap_text=True)
    ws1[f'F{r_idx}'].border = border_cell
    
    ws1[f'G{r_idx}'] = r_data[6]
    ws1[f'G{r_idx}'].font = Font(name='Calibri', size=10, bold=True, color=GREEN_TEXT)
    ws1[f'G{r_idx}'].alignment = Alignment(horizontal='center', vertical='center')
    ws1[f'G{r_idx}'].border = border_cell

# Anchos de columna Hoja 1
col_widths_ws1 = {'A': 22, 'B': 30, 'C': 32, 'D': 32, 'E': 28, 'F': 30, 'G': 20}
for col, width in col_widths_ws1.items():
    ws1.column_dimensions[col].width = width

# ==========================================
# HOJA 2: RESUMEN EJECUTIVO COPQ & FINANZAS
# ==========================================
ws2 = wb.create_sheet(title='Resumen_Ejecutivo_COPQ')
ws2.views.sheetView[0].showGridLines = True

ws2.merge_cells('A2:F2')
ws2['A2'] = 'CUADRO EJECUTIVO: COSTO DE NO CALIDAD (COPQ) Y RETORNO FINANCIERO'
ws2['A2'].font = font_title
ws2['A2'].alignment = Alignment(vertical='center')

ws2.merge_cells('A3:F3')
ws2['A3'] = 'Auditoría de 10,000 Eventos de Producción | Ahorro a Capex Cero por Optimización de Decisiones de Calidad'
ws2['A3'].font = font_subtitle

# Sección 1: Costo por Desenlace Operativo
ws2.merge_cells('A5:E5')
ws2['A5'] = '1. MATRIZ DE COSTO UNITARIO SEGÚN DESENLACE OPERATIVO'
ws2['A5'].font = font_sec_header
ws2['A5'].fill = fill_sec
ws2['A5'].alignment = Alignment(horizontal='center', vertical='center')

cost_headers = ['Desenlace Operativo', 'Eventos en Muestra', 'Costo Medio USD', 'Costo Total USD', 'Comportamiento en Planta']
for i, ch in enumerate(cost_headers):
    col = ['A', 'B', 'C', 'D', 'E'][i]
    ws2[f'{col}6'] = ch
    ws2[f'{col}6'].font = font_col_header
    ws2[f'{col}6'].fill = fill_subhdr
    ws2[f'{col}6'].alignment = Alignment(horizontal='center', vertical='center')
    ws2[f'{col}6'].border = border_cell

cost_rows = [
    ('1. Aprobado Directo', 6728, 23.54, '=B7*C7', 'Flujo de calidad conforme a primera pasada (Right First Time).'),
    ('2. Retrabajo Exitoso', 2033, 36.67, '=B8*C8', 'Recuperación económica rentable en banco auxiliar.'),
    ('3. Scrap Directo', 57, 101.31, '=B9*C9', 'Pérdida de material contenida inmediatamente.'),
    ('4. Retrabajo Fallido (Scrap)', 191, 126.78, '=B10*C10', 'PÉRDIDA DOBLE: Material destruido + mano de obra + energía.')
]

for idx, cr in enumerate(cost_rows, start=7):
    ws2[f'A{idx}'] = cr[0]
    ws2[f'A{idx}'].font = font_bold
    ws2[f'A{idx}'].border = border_cell
    
    ws2[f'B{idx}'] = cr[1]
    ws2[f'B{idx}'].font = font_val
    ws2[f'B{idx}'].alignment = Alignment(horizontal='center')
    ws2[f'B{idx}'].border = border_cell
    
    ws2[f'C{idx}'] = cr[2]
    ws2[f'C{idx}'].font = font_bold
    ws2[f'C{idx}'].number_format = '$#,##0.00'
    ws2[f'C{idx}'].alignment = Alignment(horizontal='right')
    ws2[f'C{idx}'].border = border_cell
    
    ws2[f'D{idx}'] = cr[3]
    ws2[f'D{idx}'].font = font_bold
    ws2[f'D{idx}'].number_format = '$#,##0.00'
    ws2[f'D{idx}'].alignment = Alignment(horizontal='right')
    ws2[f'D{idx}'].border = border_cell
    
    ws2[f'E{idx}'] = cr[4]
    ws2[f'E{idx}'].font = Font(name='Calibri', size=9, italic=True)
    ws2[f'E{idx}'].border = border_cell

# Destacar fila 4 en rojo
for col in ['A', 'B', 'C', 'D']:
    ws2[f'{col}10'].fill = PatternFill(start_color=RED_FILL, end_color=RED_FILL, fill_type='solid')

# Sección 2: KPIs de Impacto Financiero
ws2.merge_cells('A13:E13')
ws2['A13'] = '2. CUANTIFICACIÓN DEL IMPACTO FINANCIERO AHORRADO'
ws2['A13'].font = font_sec_header
ws2['A13'].fill = fill_sec
ws2['A13'].alignment = Alignment(horizontal='center', vertical='center')

kpi_table = [
    ('Piezas en Scrap Doble Costo Erradicadas:', 191, 'Unidades severas no reprocesadas'),
    ('Sobrecosto Evitado por Unidad:', 25.47, 'Diferencia ($126.78 - $101.31 USD)'),
    ('Ahorro Neto Auditado en Muestra (10k eventos):', '=B14*B15', 'Ahorro directo inmediato'),
    ('Horas Hombre Productivas Recuperadas:', 78.0, 'Horas de operario devueltas a línea'),
    ('Ahorro Anualizado Proyectado (100k eventos/año):', '=B16*10', 'Impacto EBITDA anual a Capex Cero')
]

for idx, (lbl, val, note) in enumerate(kpi_table, start=14):
    ws2[f'A{idx}'] = lbl
    ws2[f'A{idx}'].font = font_label
    ws2[f'A{idx}'].border = border_cell
    
    ws2[f'B{idx}'] = val
    ws2[f'B{idx}'].font = Font(name='Calibri', size=11, bold=True, color=GREEN_TEXT if idx in [16, 18] else '000000')
    if idx in [15, 16, 18]:
        ws2[f'B{idx}'].number_format = '$#,##0.00'
    ws2[f'B{idx}'].alignment = Alignment(horizontal='center')
    ws2[f'B{idx}'].border = border_cell
    
    ws2.merge_cells(f'C{idx}:E{idx}')
    ws2[f'C{idx}'] = note
    ws2[f'C{idx}'].font = Font(name='Calibri', size=9, italic=True, color='667085')
    ws2[f'C{idx}'].border = border_cell
    ws2[f'D{idx}'].border = border_cell
    ws2[f'E{idx}'].border = border_cell

col_widths_ws2 = {'A': 42, 'B': 20, 'C': 22, 'D': 22, 'E': 45}
for col, width in col_widths_ws2.items():
    ws2.column_dimensions[col].width = width

wb.save('entregables_planta/Matriz_Decision_Retrabajo_Piso.xlsx')
print('[OK] Matriz Excel regenerada exitosamente como OPL y Tablero COPQ.')
