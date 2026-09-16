# 📋 PROJECT TRACKER: Control de Calidad, Scrap y Retrabajo (Enfoque Industrial)

Este tablero registra el avance y entrega de cada pieza del Proyecto 03, asegurando rigor técnico, aplicabilidad real en planta y alta credibilidad ante Gerentes de Operaciones y Directores de Calidad.

---

## 📌 Estado General del Proyecto
* **Proyecto:** 03_Control_Calidad_Scrap_Retrabajo
* **Enfoque:** Six Sigma DMAIC + Gestión de COPQ + Dashboard Ejecutivo en Código + Reporte A3 Lean + OPL de Piso
* **Estado:** 🟢 100% Completado & Verificado
* **Ahorro Demostrado:** +$4,878.44 USD netos en muestra (+$48,648 USD/año proyectados) a Capex Cero
* **Capacidad Recuperada:** +78.0 horas de operario devueltas a línea productiva

---

## 🗺️ Mapa de Entregables y Checklist por Nivel de Gestión

### 🏛️ Nivel 1: Dirección y Gerencia de Planta (Dashboard Ejecutivo & Finanzas COPQ)
- [x] **Dashboard Web en Código Nativo ([`server.py`](server.py) & [`templates/index.html`](templates/index.html)):**
  - [x] Backend FastAPI + DuckDB en memoria sirviendo endpoints analíticos de alta velocidad en milisegundos.
  - [x] Interfaz ejecutiva moderna con Tailwind CSS y ApexCharts con paleta corporativa (`#1B365D` navy).
  - [x] Segmentadores dinámicos por Planta, Línea y Turno con actualización reactiva sin recarga de página.
  - [x] Navegación entre 3 vistas: (1) Resumen Ejecutivo COPQ, (2) Causa Raíz & Desempeño Operativo, (3) Eficacia Inspección & Blindaje Garantía.
  - [x] Tabla interactiva de auditoría de eventos de calidad con buscador en tiempo real y badges de severidad.
- [x] **Dataset Enriquecido para BI (`data/processed/powerbi_calidad_copq.csv`):**
  - [x] 10,000 registros con variables calculadas: Categoría COPQ (Falla Interna, Externa, Evaluación), Desenlace Operativo, Costo Pérdida Doble, Rangos de Velocidad y Rangos de Antigüedad.
- [x] **Especificación Oficial de Power BI ([`powerbi/ESPECIFICACION_DASHBOARD_POWERBI.md`](powerbi/ESPECIFICACION_DASHBOARD_POWERBI.md)):**
  - [x] Arquitectura de datos estrella (`FactCalidad` vinculada a dimensiones de tiempo, línea, defecto e inspección).
  - [x] Diccionario completo de medidas DAX (`[COPQ Total USD]`, `[Tasa Scrap %]`, `[Tasa Retrabajo %]`, `[Tasa Escape Garantía %]`, `[Ahorro Proyectado Anual USD]`).
  - [x] Wireframes y capturas de diseño de las 3 páginas en `powerbi/capturas_dashboard/`.

---

### 🔬 Nivel 2: Ingeniería de Procesos & Six Sigma (Reporte A3 de Lean Manufacturing)
- [x] **Reporte A3 Formal ([`entregables_planta/Reporte_A3_Resolucion_Problemas_Calidad.md`](entregables_planta/Reporte_A3_Resolucion_Problemas_Calidad.md)):**
  - [x] Estructurado bajo la metodología oficial de Toyota (7 bloques: Antecedentes, Condición Actual, Metas SMART, Análisis Causa Raíz Ishikawa 4M + 5 Porqués, Contramedidas CAPA, Confirmación de Efectos y Estandarización).
  - [x] Cuantificación de la trampa del retrabajo severo ($126.78 USD vs $101.31 USD).
  - [x] Demostración de las 3 causas raíz: velocidad forzada (+49% defectos), máquinas >8 años (+63% fallas) y fuga de inspección manual (1.61% vs 0.93%).
- [x] **Notebook Estadístico Ejecutado ([`notebooks/01_control_calidad_copq_y_decision.ipynb`](notebooks/01_control_calidad_copq_y_decision.ipynb)):**
  - [x] Análisis exploratorio y pruebas estadísticas sobre 10,000 eventos reales.
  - [x] Gráficos ejecutivos exportados en `data/processed/` (`grafico_costo_desenlace.png`, `grafico_severidad_retrabajo.png`, `grafico_causas_raiz.png`).

---

### 🏭 Nivel 3: Operación y Piso de Planta (One-Point Lesson & Matriz Física)
- [x] **One-Point Lesson Plastificada ([`entregables_planta/OPL_Criterios_Calidad_Piso.md`](entregables_planta/OPL_Criterios_Calidad_Piso.md)):**
  - [x] Estándar visual de 1 sola página para ubicar a pie de máquina en estaciones de inspección.
  - [x] Criterios físicos y tolerancias medibles para 5 tipos de defecto clasificados en 3 severidades.
  - [x] Flujo físico de 3 gavetas: Verde (Reproceso en banco), Amarilla (Cuarentena / Supervisor) y Roja (Scrap directo e irreversible).
- [x] **Libro Excel de Piso & Resumen Financiero ([`entregables_planta/Matriz_Decision_Retrabajo_Piso.xlsx`](entregables_planta/Matriz_Decision_Retrabajo_Piso.xlsx)):**
  - [x] Hoja 1: `OPL_Criterios_Calidad_Piso` formateada para impresión directa en hoja membretada.
  - [x] Hoja 2: `Resumen_Ejecutivo_COPQ` con desglose de costos por desenlace y fórmulas de retorno económico.

---

### 🎙️ Nivel 4: Estrategia de Entrevista Laboral y Venta del Perfil
- [x] **Guía Maestra para Entrevistas ([`EXPLICACION_PASO_A_PASO_PROYECTO.md`](EXPLICACION_PASO_A_PASO_PROYECTO.md)):**
  - [x] Pitch de 30 segundos (Elevator Pitch) y 2 minutos (Estructura STAR).
  - [x] Las 3 cifras clave a memorizar.
  - [x] Respuestas a las 7 preguntas más desafiantes de Gerentes de Planta y Directores de Calidad.
  - [x] Alineación con la experiencia real en laboratorio de calidad (Agua Azul e Incarpalm).