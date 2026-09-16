# 📄 Ficha Ejecutiva del Proyecto (Formato STAR / CAR)
## Optimización del Costo de No Calidad (COPQ) y Reducción de Scrap mediante Semáforo de Piso
**Candidato:** Angelo Apolo | Ing. Químico / Industrial | Máster en Dirección de Proyectos  
**Target:** Jefe de Aseguramiento de Calidad (QA/QC), Ingeniero de Procesos / Six Sigma, Coordinador de Operaciones  

---

### 1. Situación (Situation)
* En una planta manufacturera de alta cadencia (10,000 eventos evaluados), el equipo de supervisión de piso enfrentaba una alta dispersión en las decisiones de calidad: **el 24.3% de la producción era desviada a reproceso (rework)** sin criterios técnicos ni financieros estandarizados.
* Esta falta de estandarización generaba una "trampa silenciosa de costos": **191 piezas retrabajadas terminaban siendo descartadas a chatarra (scrap) de todas formas**, duplicando el costo unitario a **$126.78 USD** (frente a $101.31 USD de scrap directo) y desperdiciando ~78 horas de trabajo operativo en línea.
* Además, la inspección manual presentaba una tasa de fuga a cliente de 1.61%, un 70% superior a los métodos automatizados por sensor y visión artificial.

---

### 2. Tarea (Task)
* **Objetivo Principal:** Eliminar el retrabajo a ciegas y erradicar las piezas enviadas a scrap tras reproceso fallido.
* **Meta Operativa:** Diseñar e implementar una herramienta de piso accesible para inspectores y supervisores que clasifique en segundos si un defecto debe retrabajarse o enviarse a descarte inmediato.
* **Meta Financiera:** Reducir el Costo de No Calidad (COPQ) a Capex Cero, liberando horas productivas de cuadrilla y blindando la entrega para minimizar reclamos en garantía a 90 días.

---

### 3. Acción (Action)
* **Auditoría Estadística y Causas Raíz:**
  * Mediante pruebas de contingencia $\chi^2$ y análisis de varianza, se aislaron los 3 detonantes físicos del defecto: forzamiento de velocidad de línea (>139 u/h disparaba +49% defectos), envejecimiento de activos (>8 años duplicaba fallas) y materias primas Grado C (+40% defectos).
* **Modelo Predictivo de Éxito de Retrabajo:**
  * Se modeló la probabilidad de aprobación final ($P(\text{Final Pass} = 1)$) en función del tipo de defecto, severidad (0 a 3), método de inspección y desgaste del equipo (ROC-AUC = 0.81).
* **Diseño del "Semáforo de Decisión en Piso" (Excel + Web App):**
  * **🟢 VERDE (Retrabajar - $P \ge 75\%$):** Defectos leves de dimensión o acabado en equipos estables. Éxito real comprobado del 87.8% con beneficio neto positivo.
  * **🟡 AMARILLO (Evaluar - $55\% \le P < 75\%$):** Defectos moderados que solo se autorizan con velocidad controlada.
  * **🔴 ROJO (Scrap Directo - $P < 55\%$):** Defectos severos (Severidad 3 en grietas y fracturas). Se prohíbe el retrabajo de inmediato para no tirar dinero bueno sobre dinero malo.
* **Estandarización y Protocolo CAPA 8D:**
  * Implementación de una plantilla Excel interactiva de 1 sola página para uso diario del inspector y un plan de acción correctiva 8D enfocado en control de velocidad de máquina y lubricación preventiva.

---

### 4. Resultados Cuantificables (Results)
| Indicador Clave de Desempeño | Antes (Línea Base) | Después (Con Semáforo) | Impacto para el Negocio |
|---|:---:|:---:|:---:|
| **Scrap de Doble Costo (Post-retrabajo)** | 191 unidades ($126.78 USD c/u) | **0 unidades** | **Eliminación total de la peor pérdida de planta** |
| **Ahorro Directo Inmediato (10k eventos)** | Baseline de pérdidas | **+$4,863.79 USD netos** | Ahorro a Capex Cero ($25.47 USD por pieza filtrada) |
| **Ahorro Proyectado Fábrica (100k eventos/año)** | — | **+$48,638 USD / año** | Impacto directo en el EBITDA operativo |
| **Capacidad y Horas Hombre Recuperadas** | 78 h desperdiciadas | **+78 h operativas devueltas** | Mayor productividad y descongestión de líneas |
| **Fugas a Reclamos de Garantía (90 días)** | 1.61% en inspección manual | **< 1.00% con visión/sensores** | **-38% en riesgo de penalización y reclamos de cliente** |

---

### 💡 Pregunta Rápida para Entrevistas:
> **"¿Por qué es preferible enviar una pieza defectuosa a scrap directo en lugar de intentar arreglarla?"**  
> *"Porque en manufactura, retrabajar un defecto severo tiene una probabilidad de fracaso superior al 50%. En nuestra planta comprobamos que la pieza retrabajada que termina en scrap cuesta $126.78 USD vs. $101.31 USD de scrap directo. Retrabajar a ciegas significa pagar el valor de la pieza dos veces más el sueldo del operario. La verdadera excelencia de calidad consiste en saber cuándo cortar la pérdida a tiempo."*
