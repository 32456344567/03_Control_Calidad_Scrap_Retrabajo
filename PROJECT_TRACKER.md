# 📋 PROJECT TRACKER: Control de Calidad, Scrap y Retrabajo (Lean & Sellable)

Este tablero registra el avance y entrega de cada pieza del Proyecto 03, asegurando simplicidad ejecutiva, alto impacto visual y aplicabilidad directa en piso de planta.

---

## 📌 Estado General del Proyecto
* **Proyecto:** 03_Control_Calidad_Scrap_Retrabajo
* **Enfoque:** Six Sigma DMAIC + Matriz de Decisión Financiera (Retrabajo vs. Scrap) + Semáforo Interactivo
* **Estado:** 🟢 100% Completado & Verificado
* **Ahorro Demostrado:** +$4,864 USD netos en muestra (+$48,648 USD anuales proyectados) a Capex Cero

---

## 🗺️ Mapa de Entregables y Checklist

### 🧪 Nivel 1: Datos, Costo de Calidad (COPQ) y Modelo de Decisión
- [x] **Configuración base y entorno:**
  - [x] Carpetas base (`notebooks/`, `src/`, `entregables_planta/`, `templates/`, `static/`, `docs/`).
  - [x] Requerimientos (`requirements.txt`), `Procfile`, `.gitignore`.
- [x] **Notebook Ejecutivo (`notebooks/01_control_calidad_copq_y_decision.ipynb`):**
  - [x] Exploración y diagnóstico de 10,000 eventos (defectos, severidades, métodos).
  - [x] Cuantificación del Costo de No Calidad (COPQ) y análisis de la trampa del retrabajo severo ($126.78 USD vs $101.31 USD).
  - [x] Identificación de causas operativas (velocidad excesiva +49% defectos, antigüedad de activos +63% defectos, grado de material).
  - [x] Modelo de probabilidad de éxito ($P(\text{Final Pass} = 1)$) y regla de decisión financiera $\mathbb{E}[\text{Beneficio}]$.
  - [x] Exportación de métricas consolidadas (`data/processed/resumen_kpis_calidad.json`) y 3 gráficos ejecutivos.

### 🏭 Nivel 2: Entregables Prácticos de Planta (`entregables_planta/`)
- [x] **Matriz Excel de Decisión en Piso (`Matriz_Decision_Retrabajo_Piso.xlsx`):**
  - [x] Herramienta interactiva de 1 sola página con semáforo automatizado para supervisores de línea.
  - [x] Fórmulas dinámicas de costo esperado, beneficio neto y matriz visual por tipo de defecto.
- [x] **Ficha Ejecutiva STAR (`Ficha_Ejecutiva_STAR_Proyecto.md`):**
  - [x] Resumen ejecutivo de 1 página con el storytelling comercial para CV, LinkedIn y entrevistas laborales.
- [x] **Protocolo CAPA / 8D (`Protocolo_CAPA_8D_Visual.md`):**
  - [x] Plan formal de contención, análisis de causa raíz (Ishikawa 4M + 5 Porqués) y acciones preventivas.

### 🌐 Nivel 3: Aplicación Web Interactiva (Semáforo en Piso)
- [x] **Servidor y API (`server.py`):**
  - [x] Endpoints de cálculo en vivo de decisión (`/api/decide`) y descarga de plantilla (`/download/excel`).
  - [x] Verificado localmente con código HTTP 200 y lógica de contingencia.
- [x] **Interfaz de Usuario (`templates/index.html`):**
  - [x] Tarjetas KPI ejecutivas de impacto (Ahorro directo, Horas recuperadas, Scrap de doble costo erradicado).
  - [x] Simulador interactivo tipo semáforo en tiempo real con barra de probabilidad y dictamen inmediato.
  - [x] Gráficos interactivos Chart.js de costo por desenlace y efectividad por severidad.

### 📖 Nivel 4: Guía Maestra de Entrevistas Laborales
- [x] **Guía de Entrevista (`EXPLICACION_PASO_A_PASO_PROYECTO.md`):**
  - [x] Pitch de 30 segundos (Elevator Pitch) y 2 minutos (Estructura STAR).
  - [x] Las 3 cifras clave a memorizar.
  - [x] Respuestas modelo a las 7 preguntas más difíciles de Directores de Planta y Gerentes de Calidad.
  - [x] Vínculo con la experiencia real en laboratorio de calidad (Agua Azul e Incarpalm).
