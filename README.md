# 🎯 Decisiones de Calidad, Scrap y Costo de Retrabajo
## Optimización Financiera del Costo de No Calidad (COPQ) mediante Semáforo Operativo de Piso
**Proyecto 03 | Portafolio Técnico de Operaciones, Procesos y Calidad Industrial**  
**Autor:** Angelo Apolo | Ing. Químico / Industrial | Máster en Dirección de Proyectos y Empresas  
**Target Profesional:** Jefe / Ingeniero de Aseguramiento de Calidad (QA/QC), Ingeniero de Procesos / Six Sigma, Coordinador de Operaciones  

---

## 💡 El Dilema de Planta en 30 Segundos
En piso de producción, cuando un inspector detecta una pieza defectuosa se enfrenta al dilema diario:
* **¿Se envía a Scrap directo?** (Se pierde el material de inmediato, costo unitario ~$101.31 USD).
* **¿Se autoriza Retrabajo?** (Se invierte tiempo de operario y energía, pero si el defecto es severo, más del 50% fracasa y la pieza igual termina en scrap con un costo disparado a **$126.78 USD**).

Este proyecto analiza **10,000 eventos reales de manufactura** para erradicar el retrabajo a ciegas, sustituyéndolo por un **Semáforo de Decisión en Piso** que maximiza el beneficio económico a Capex Cero.

---

## 📊 Las 3 Cifras Clave del Proyecto
1. **$126.78 USD vs. $101.31 USD:** Sobrecosto evitado por cada pieza severa que no se somete a reproceso inviable (**+$25.47 USD de ahorro neto por pieza**).
2. **+$4,863.79 USD en la muestra / +$48,648 USD al año:** Ahorro financiero proyectado para una operación de 100,000 eventos anuales.
3. **+78.0 Horas Hombre Devueltas:** Capacidad productiva recuperada en líneas de ensamble y calidad.

---

## 🛠️ Stack Tecnológico & Metodología
* **Six Sigma DMAIC:** Mapeo de fallas internas, costos de evaluación y fallas externas (reclamos de garantía a 90 días).
* **Python (Data Science & ML):** Regresión logística multivariable para estimar $P(\text{Final Pass} = 1)$ con ROC-AUC = 0.81.
* **Herramientas de Piso:** Hoja Excel interactiva de 1 página (`Matriz_Decision_Retrabajo_Piso.xlsx`) con semáforo automatizado.
* **Aplicación Web Interactiva:** Servidor en Flask (`server.py`) con simulador semáforo en vivo y gráficos ejecutivos (Chart.js), listo para desplegar en Railway.

---

## 📁 Estructura del Repositorio

```text
03_Control_Calidad_Scrap_Retrabajo/
├── README.md                                  <-- Este documento ejecutivo
├── PROJECT_TRACKER.md                        <-- Checklist y estado de avance
├── EXPLICACION_PASO_A_PASO_PROYECTO.md       <-- Guía maestra para entrevistas (10 min de lectura ágil)
├── server.py                                 <-- Aplicación web interactiva (Simulador Semáforo)
├── requirements.txt & Procfile               <-- Configuración para despliegue en la nube
├── data/
│   ├── manufacturing_quality_decisions_10000.csv <-- Dataset oficial de 10k registros
│   ├── README_DATA.md                        <-- Ficha técnica de variables
│   └── processed/                            <-- Métricas consolidadas y gráficos
├── notebooks/
│   └── 01_control_calidad_copq_y_decision.ipynb <-- Notebook ejecutivo integral con salidas ejecutadas
├── entregables_planta/
│   ├── Matriz_Decision_Retrabajo_Piso.xlsx   <-- Herramienta interactiva de piso para supervisores
│   ├── Ficha_Ejecutiva_STAR_Proyecto.md      <-- Resumen de 1 página para CV y LinkedIn
│   └── Protocolo_CAPA_8D_Visual.md           <-- Protocolo de contención y causa raíz (8 Disciplines)
└── templates/
    └── index.html                            <-- Interfaz moderna del semáforo en vivo
```

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Lanzar la Aplicación Web Interactiva:**
   ```bash
   py server.py
   ```
   Abre tu navegador en `http://localhost:5000` para interactuar con el **Semáforo de Decisión en Piso** y probar diferentes escenarios de severidad, defecto y velocidad de línea.

3. **Abrir la Herramienta Excel de Piso:**
   * Abre `entregables_planta/Matriz_Decision_Retrabajo_Piso.xlsx` para ver cómo los supervisores ingresan parámetros y obtienen el semáforo automático con fórmulas de costo.

---

## 🤝 Autor & Contacto
* **Ing. Angelo Apolo**
* Ingeniero Químico / Industrial | Máster en Dirección de Proyectos
* Especialista en Operaciones, Aseguramiento de Calidad (QA/QC) y Six Sigma
