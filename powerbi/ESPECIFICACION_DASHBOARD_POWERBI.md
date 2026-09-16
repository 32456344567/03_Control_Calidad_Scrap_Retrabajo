# 📊 Especificación de Ingeniería: Tablero Gerencial Power BI
## Cuadro de Mando Ejecutivo: Control de Calidad, Scrap y Costos COPQ
**Proyecto 03 | Portafolio Técnico de Operaciones y Calidad Industrial**  
**Autor:** Angelo Apolo | Ing. Químico / Industrial | Máster en Dirección de Proyectos  
**Audiencia Objetivo:** Gerente de Planta, Director de Operaciones, Jefe de Aseguramiento de Calidad (QA/QC)  

---

## 🎯 1. Propósito Gerencial del Tablero
Este cuadro de mando traslada los datos de 10,000 eventos de producción a un formato de **decisión ejecutiva**:
* **Visibilidad Financiera (COPQ):** Permite a la Gerencia saber exactamente cuánto dinero se fuga en Falla Interna (Scrap + Retrabajo) vs. Falla Externa (Garantías de clientes).
* **Estratificación Operativa:** Identifica de forma inmediata qué plantas, líneas de producción y turnos concentran el desperdicio.
* **Control de Fugas a Cliente:** Evalúa la efectividad de la inspección manual frente a visión artificial y sensores ópticos para erradicar penalizaciones de calidad.

---

## 🏗️ 2. Modelo de Datos (Esquema Estrella)

```text
       ┌──────────────┐             ┌──────────────┐
       │  DimPlanta   │             │  DimTurno    │
       ├──────────────┤             ├──────────────┤
       │ plant_id     │             │ shift_id     │
       └──────┬───────┘             └──────┬───────┘
              │ 1                          │ 1
              │                            │
              ▼ *                          ▼ *
      ┌────────────────────────────────────────────┐
      │          FactCalidad (10,000 filas)        │
      ├────────────────────────────────────────────┤
      │ event_id (PK)                              │
      │ event_ts, plant, line, shift               │
      │ machine_id, machine_age_yrs                │
      │ material_grade, process_speed_units_hr     │
      │ inspection_method, defect_type, severity   │
      │ decision_rework, final_pass, scrap         │
      │ warranty_claim_90d, cost_usd               │
      │ categoria_copq, desenlace_operativo        │
      │ costo_perdida_doble                        │
      └────────────────────────────────────────────┘
              ▲ *                          ▲ *
              │                            │
              │ 1                          │ 1
       ┌──────┴───────┐             ┌──────┴───────┐
       │  DimDefecto  │             │ DimInspeccion│
       ├──────────────┤             ├──────────────┤
       │ defect_type  │             │ method_name  │
       │ severity     │             │ tech_type    │
       └──────────────┘             └──────────────┘
```

* **Fuente de Datos:** `data/processed/powerbi_calidad_copq.csv` (10,000 filas, 29 columnas enriquecidas).

---

## 📐 3. Diccionario Oficial de Medidas DAX

### A. Métricas de Volumen e Integridad
```dax
Total Eventos = 
COUNTROWS('FactCalidad')
```

```dax
Piezas Aprobadas = 
CALCULATE(
    COUNTROWS('FactCalidad'),
    'FactCalidad'[final_pass] = 1
)
```

```dax
Tasa Aprobacion % = 
DIVIDE([Piezas Aprobadas], [Total Eventos], 0)
```

---

### B. Métricas de Scrap y Retrabajo (Falla Interna)
```dax
Unidades Scrap = 
CALCULATE(
    COUNTROWS('FactCalidad'),
    'FactCalidad'[scrap] = 1
)
```

```dax
Tasa Scrap % = 
DIVIDE([Unidades Scrap], [Total Eventos], 0)
```

```dax
Unidades Retrabajadas = 
CALCULATE(
    COUNTROWS('FactCalidad'),
    'FactCalidad'[decision_rework] = 1
)
```

```dax
Tasa Retrabajo % = 
DIVIDE([Unidades Retrabajadas], [Total Eventos], 0)
```

```dax
Exito Retrabajo % = 
CALCULATE(
    DIVIDE(
        CALCULATE(COUNTROWS('FactCalidad'), 'FactCalidad'[final_pass] = 1),
        COUNTROWS('FactCalidad'),
        0
    ),
    'FactCalidad'[decision_rework] = 1
)
```

---

### C. Métricas Financieras y Costo de No Calidad (COPQ)
```dax
Costo Total Eventos USD = 
SUM('FactCalidad'[cost_usd])
```

```dax
COPQ Falla Interna USD = 
CALCULATE(
    SUM('FactCalidad'[cost_usd]),
    'FactCalidad'[categoria_copq] IN {"Falla Interna (Scrap)", "Falla Interna (Retrabajo)"}
)
```

```dax
COPQ Falla Externa USD = 
CALCULATE(
    SUM('FactCalidad'[cost_usd]),
    'FactCalidad'[categoria_copq] = "Falla Externa (Reclamo Garantía)"
)
```

```dax
COPQ Total USD = 
[COPQ Falla Interna USD] + [COPQ Falla Externa USD]
```

```dax
Costo Medio Unidad USD = 
DIVIDE([Costo Total Eventos USD], [Total Eventos], 0)
```

```dax
Perdida Retrabajo Fallido USD = 
SUM('FactCalidad'[costo_perdida_doble])
```

```dax
Ahorro Proyectado Anual USD = 
[Perdida Retrabajo Fallido USD] * 10
```

---

### D. Métricas de Calidad ante Cliente (Falla Externa)
```dax
Reclamos Garantia 90d = 
CALCULATE(
    COUNTROWS('FactCalidad'),
    'FactCalidad'[warranty_claim_90d] = 1
)
```

```dax
Tasa Escape Garantia % = 
DIVIDE([Reclamos Garantia 90d], [Total Eventos], 0)
```

---

## 🖥️ 4. Estructura y Vistas de las 3 Páginas Ejecutivas

### Página 1: Resumen Ejecutivo de Calidad & Costo de No Calidad (COPQ)
* **Objetivo:** Vista para el Director de Planta y Gerente de Operaciones.
* **Filtros Superiores:** Planta (`plant_1`, `plant_2`), Línea (`line_A`, `line_B`), Turno (`day`, `swing`, `graveyard`).
* **Tarjetas KPI Principales:**
  1. `COPQ Total USD` (Formato Moneda `$#,##0`).
  2. `Tasa Scrap %` (Meta: < 2.0% | Semaforización: Verde <2%, Rojo ≥2%).
  3. `Tasa Retrabajo %` (Línea base: 24.3%).
  4. `Reclamos de Garantía` (Total: 125 eventos | Tasa: 1.25%).
  5. `Ahorro Proyectado Anual USD` (+$48,648 USD a Capex Cero).
* **Visual 1 (Donut Chart):** Composición del COPQ (Falla Interna Scrap vs Falla Interna Retrabajo vs Falla Externa Garantía).
* **Visual 2 (Gráfico de Columnas Agrupadas):** Costo Medio Unitario según Desenlace Operativo:
  * Aprobado Directo: $23.54 USD.
  * Retrabajo Exitoso: $36.67 USD.
  * Scrap Directo: $101.31 USD.
  * Retrabajo Fallido (Scrap): **$126.78 USD** (¡Destacado en rojo corporativo!).
* **Visual 3 (Matriz / Tabla):** Resumen de KPI por Planta y Línea con semáforos condicionales.

---

### Página 2: Análisis Causa Raíz & Desempeño de Piso
* **Objetivo:** Vista para el Ingeniero de Procesos y Black Belt / Green Belt.
* **Visual 1 (Diagrama de Pareto 80/20):** Defectos por Costo Total Incurrido (`dimension`, `crack`, `scratch`, `finish`, `contamination`).
* **Visual 2 (Matriz de Varianza):** Defectos según Severidad (1, 2, 3) vs Tasa de Éxito de Retrabajo:
  * Severidad 1: 87.8% Éxito | 0.0% Scrap.
  * Severidad 2: 70.6% Éxito | 19.0% Scrap.
  * Severidad 3: **48.3% Éxito | 31.5% Scrap** (La justificación de corte de retrabajo).
* **Visual 3 (Dispersión / Barras):** Tasa de Defectos según Velocidad de Línea (Baja, Nominal, Alta, Forzada >139 u/h).
* **Visual 4 (Barras):** Tasa de Defectos según Antigüedad del Activo (<4 años vs >8 años).

---

### Página 3: Eficacia de Inspección & Blindaje ante Cliente
* **Objetivo:** Vista para el Jefe de Aseguramiento de Calidad (QA/QC).
* **Visual 1 (Barras Horizontales):** Tasa de Escape a Reclamo de Garantía por Método de Inspección:
  * Manual: **1.61%** (Fuga crítica de defectos).
  * Visión Artificial: **1.05%** (-35% fuga).
  * Sensor Óptico: **0.93%** (-42% fuga).
* **Visual 2 (Treemap):** Distribución de Reclamos en Garantía por Tipo de Defecto no detectado a tiempo.
* **Visual 3 (Tabla de Auditoría):** Eventos con fuga a garantía detallando máquina, turno y operador para trazabilidad CAPA.

---

## 🚀 5. Instrucciones para Importación en Power BI Desktop

1. Abre **Power BI Desktop**.
2. Selecciona **Obtener Datos -> Texto/CSV** y carga el archivo:
   `data/processed/powerbi_calidad_copq.csv`
3. En la vista de Modelo, crea una tabla de medidas llamada `_Medidas_Calidad` y copia las fórmulas DAX del Punto 3.
4. Diseña las páginas siguiendo la distribución del Punto 4 utilizando la paleta institucional (Azul Marino `#1B365D`, Verde Éxito `#10B981`, Ámbar Advertencia `#F59E0B` y Rojo Alerta `#EF4444`).
