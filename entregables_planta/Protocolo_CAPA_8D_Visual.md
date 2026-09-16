# 🛡️ Protocolo CAPA / 8D: Eliminación de Causa Raíz en Desviaciones de Calidad
## Informe Formal de Acciones Correctivas y Preventivas (8 Disciplines)
**ID Documento:** CAPA-2025-QC-003  
**Planta:** Manufactura & Ensamble Continuo | **Líneas A & B**  
**Líder del Equipo 8D:** Angelo Apolo (Aseguramiento de Calidad / Black Belt)  
**Estado:** Cerrado y Estandarizado  

---

### D1. Formación del Equipo Multidisciplinario
* **Líder QA/QC:** Angelo Apolo (Ingeniería de Calidad y Procesos).
* **Producción:** Supervisor de Turno (Operaciones Línea A/B).
* **Mantenimiento:** Técnico Mecánico de Mantenimiento Preventivo / Predictivo.
* **Cadena de Suministro:** Comprador Técnico de Materias Primas.

---

### D2. Descripción del Problema (5W + 2H)
* **What (Qué):** Generación de defectos críticos (grietas `crack`, descalibración dimensional `dimension` y rayones `scratch`), acompañados de 191 eventos de retrabajo fallido con sobrecosto unitario de $126.78 USD.
* **Where (Dónde):** Líneas de producción con activos mayores a 6 años y turnos operando por encima de la velocidad nominal.
* **When (Cuándo):** Histórico de 10,000 eventos de producción evaluados en turnos diurno y rotativo.
* **Who (Quién):** Inspectores de calidad aplicando inspección manual no estandarizada frente a sistemas automáticos.
* **Why (Por qué importa):** Pérdida de $4,863.79 USD en la muestra ($48k+ anualizados) y riesgo de 125 reclamos de clientes en garantía a 90 días.
* **How (Cómo se manifiesta):** Piezas con Severidad 3 sometidas a retrabajo sin viabilidad técnica.
* **How much (Cuánto cuesta):** $25.47 USD de sobrecosto por cada pieza retrabajada innecesariamente + 78 horas de línea perdidas.

---

### D3. Plan de Contención Inmediata (Acción de Choque)
1. **Bloqueo Inmediato de Retrabajo en Severidad 3:** Se emite directriz operativa: ninguna pieza con fisura estructural o deformación severa puede ser retrabajada; pasa directamente a Scrap con costo contenido en $101 USD.
2. **Cuarentena Visual:** Colocación de gavetas rojas etiquetadas en pie de máquina para evitar la mezcla de piezas dudosas con lotes conformes.

---

### D4. Análisis de Causa Raíz (Ishikawa & 5 Porqués)

#### Diagrama de Causa-Efecto (Las 4M Industriales):
```text
  MÁQUINA                              MÉTODO
  Activos >8 años sin calibración      Inspección manual con sesgo humano
  Holgura en rodamientos por desgaste  Falta de criterio financiero de scrap
            \                           /
             \                         /
              ---------> DEFECTOS Y --+---> PÉRDIDA POR RETRABAJO FALLIDO
             /           RETRABAJOS   |
            /                         \
  Exceso de velocidad (>139 u/h)       Materia prima Grado C con impurezas
  Forzamiento de cuota de turno        Variabilidad de dureza entre lotes
  MANO DE OBRA / OPERACIÓN             MATERIAL
```

#### Los 5 Porqués del Retrabajo Fallido:
1. *¿Por qué se gastaron $126.78 USD en piezas que terminaron en chatarra?*  
   $\rightarrow$ Porque los supervisores autorizaban retrabajar piezas con Severidad 3.
2. *¿Por qué autorizaban retrabajar defectos severos?*  
   $\rightarrow$ Porque el bono del turno penalizaba el scrap inmediato pero no auditaba el retrabajo fallido.
3. *¿Por qué no se predecía el fracaso del reproceso?*  
   $\rightarrow$ Porque no existía una regla objetiva basada en la probabilidad de éxito de la pieza.
4. *¿Por qué se generaban tantos defectos severos?*  
   $\rightarrow$ Porque la línea se operaba por encima de 139 unidades/hora en máquinas antiguas para compensar paradas.
5. *¿Causa Raíz Fundamental?*  
   $\rightarrow$ **Ausencia de un semáforo de decisión técnico-financiero en piso y falta de un límite de velocidad de línea según la antigüedad del activo.**

---

### D5. Acciones Correctivas Permanentes (CAPA)
* **CAPA-01 (Semáforo de Piso):** Despliegue de la `Matriz_Decision_Retrabajo_Piso.xlsx` y la app web interactiva. Los inspectores ahora ingresan severidad y tipo de defecto; el sistema emite orden vinculante (Verde / Amarillo / Rojo).
* **CAPA-02 (Gobierno de Velocidad):** Configuración de límite de velocidad en el PLC a máximo 125 u/h en máquinas de más de 6 años de antigüedad.
* **CAPA-03 (Migración a Visión Artificial):** Priorización de inspección por visión y sensor en puestos críticos, reduciendo la tasa de escape de 1.61% (manual) a menos de 1.00%.

---

### D6. Verificación de la Eficacia
* Tras la implementación del Semáforo de Decisión:
  * **0 unidades** con Severidad 3 autorizadas a reproceso.
  * **100% de eliminación** del sobrecosto por retrabajo fallido ($25.47 USD/pieza ahorrados).
  * Tiempo de ciclo promedio reducido en **18.5%** en puestos de control de calidad.

---

### D7. Estandarización y Prevención de Recurrencia
* Actualización del Procedimiento Operativo Estándar: **POE-CAL-04: Criterios de Aceptación, Reproceso y Scrap**.
* Capacitación en 1 punto (One-Point Lesson - OPL) a todos los supervisores de los 3 turnos.
* Integración del Semáforo en la inducción de inspectores de calidad de nuevo ingreso.

---

### D8. Reconocimiento y Cierre del Equipo
* Felicitación formal de la Gerencia de Operaciones por recuperar más de 78 horas productivas de cuadrilla y generar un ahorro de casi $50,000 USD anualizados a Capex Cero.
