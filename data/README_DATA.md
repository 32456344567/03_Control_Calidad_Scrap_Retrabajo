# Información Oficial del Conjunto de Datos: Calidad, Scrap & Retrabajo

* **Nombre del Dataset:** Manufacturing Quality & Rework Decision Dataset
* **Origen / Autor:** William Sewell (Kaggle)
* **Licencia:** CC0: Public Domain
* **Enlace Oficial:** https://www.kaggle.com/datasets/williamsewell/manufacturing-quality-decisions

---

## 1. Resumen Ejecutivo y Contexto
Conjunto de datos estructurado a nivel de evento industrial (1 fila = 1 evento de inspección/manufactura) con **10,000 registros completos**.

El núcleo del dataset aborda el dilema crítico de toma de decisiones bajo incertidumbre en piso de planta: **métodos de inspección metrológica frente a la decisión de retrabajar (rework) versus enviar a chatarra (scrap)**, evaluando los trade-offs directos entre rendimiento de línea (*throughput*), costo incurrido, generación de mermas y riesgo de reclamos en garantía por falla externa post-entrega.

---

## 2. Características del Dataset
* **Volumen de Filas:** 10,000 eventos de producción.
* **Granularidad:** 1 fila = 1 unidad/evento de inspección y decisión.
* **Tipología de Análisis Soportados:**
  * Pruebas de hipótesis e independencia ($\chi^2$ / Fisher) entre método de inspección y aprobación final o falla en garantía.
  * Análisis de varianza (ANOVA / Kruskal-Wallis) para tiempos de ciclo y costos totales entre líneas y turnos.
  * Regresión logística multivariable para modelar la probabilidad de aprobación (`final_pass`) o riesgo de garantía a 90 días (`warranty_claim_90d`).
  * Regresión lineal multivariable para estimación del costo unitario total (`cost_usd`).

---

## 3. Diccionario Detallado de Variables

### A. Contexto de Proceso y Condiciones de Operación
| Variable | Tipo de Dato | Rango / Valores | Descripción Técnica y Relevancia en Planta |
|---|---|---|---|
| `plant` | Categórico | Identificadores de fábrica | Planta manufacturera donde se ejecutó la orden |
| `line` | Categórico | Identificadores de línea | Línea específica de producción o envasado |
| `shift` | Categórico | Turnos de trabajo | Turno operativo (evaluación de variabilidad humana y de ritmo) |
| `machine_age_yrs` | Numérico | Años | Antigüedad del activo mecánico/eléctrico (indicador de desgaste) |
| `material_grade` | Categórico | Grados de materia prima | Calidad del insumo recibido de proveedores |
| `temp_c` | Numérico | $^\circ C$ | Temperatura ambiental registrada en la nave de producción |
| `humidity_pct` | Numérico | % | Humedad relativa (afecta curado, sellado, viscosidad y propiedades) |
| `process_speed_units_hr` | Numérico | Unidades/hora | Velocidad de operación (tasa de forzamiento de máquina) |

### B. Variables de Decisión Operativa
| Variable | Tipo de Dato | Valores Posibles | Descripción Técnica |
|---|---|---|---|
| `inspection_method` | Categórico | `manual`, `sensor`, `vision` | Metodología de control de calidad aplicada en el puesto |
| `decision_rework` | Binario | `1`: Sí, `0`: No | Decisión tomada por supervisión/calidad de someter a retrabajo |

### C. Variables de Resultado e Impacto Económico
| Variable | Tipo de Dato | Valores / Unidad | Impacto Operativo y Financiero |
|---|---|---|---|
| `final_pass` | Binario | `1`: Conforme, `0`: Rechazado | Estado de aprobación final del producto |
| `scrap` | Binario | `1`: Destruido, `0`: No | Pérdida total irrecuperable de material |
| `warranty_claim_90d` | Binario | `1`: Reclamo, `0`: Sin falla | **Costo de Falla Externa:** Fuga de defecto hacia el cliente final |
| `total_cycle_time_min` | Numérico | Minutos | Tiempo total acumulado de procesamiento más inspección/reproceso |
| **`cost_usd`** | **Numérico** | **Dólares ($)** | **Costo neto final absorbido por la empresa en ese evento** |

---

## 4. Archivo Esperado en esta Carpeta
* Coloca aquí el archivo CSV descargado de Kaggle (por ejemplo: `manufacturing_quality_decisions.csv` o similar).
