# 📋 REPORTE A3: Resolución de Problemas & Reducción de Scrap
## Metodología Toyota / Lean Manufacturing para Aseguramiento de Calidad y COPQ
**ID Reporte:** A3-2025-CAL-003 | **Líder del Proyecto:** Ing. Angelo Apolo  
**Área:** Aseguramiento de Calidad & Operaciones de Planta | **Estado:** Implementado & Estandarizado  

---

```text
┌─────────────────────────────────────────────────────────┬─────────────────────────────────────────────────────────┐
│ 1. ANTECEDENTES (BACKGROUND)                            │ 5. CONTRAMEDIDAS PROPUESTAS (ACCIONES CAPA)             │
│ En plantas de manufactura continua, el 24.3% de las     │ C1. Política de Corte de Retrabajo en Severidad 3:     │
│ piezas defectuosas se envía a retrabajo sin criterio    │     Prohibición absoluta de reprocesar defectos graves. │
│ financiero estandarizado, duplicando costos.           │ C2. Límite de Velocidad en PLC:                         │
│                                                         │     Tope de 125 u/h en máquinas con más de 6 años.      │
├─────────────────────────────────────────────────────────┤ C3. One-Point Lesson (OPL) de Piso:                     │
│ 2. CONDICIÓN ACTUAL (CURRENT STATE)                     │     Tabla visual plastificada de criterios en línea.    │
│ • 191 piezas retrabajadas terminaron en Scrap.         │ C4. Migración a Visión Artificial:                      │
│ • Costo de Retrabajo Fallido: $126.78 USD vs.          │     Blindaje de inspección para bajar escape de 1.61%.  │
│   $101.31 USD de Scrap directo (+$25.47 USD / pieza).   ├─────────────────────────────────────────────────────────┤
│ • 78 horas de operario desperdiciadas en reprocesos.    │ 6. CONFIRMACIÓN DE EFECTOS (RESULTADOS AUDITADOS)       │
│ • Escape a garantía en inspección manual: 1.61%.        │ • Piezas Scrap de Doble Costo: De 191 a 0 uds (-100%).  │
├─────────────────────────────────────────────────────────┤ • Ahorro Directo (Muestra): +$4,878.44 USD netos.       │
│ 3. OBJETIVOS Y METAS (TARGET STATE)                     │ • Ahorro Proyectado Fábrica: +$48,784 USD / año.        │
│ • Erradicar al 100% el scrap post-retrabajo.            │ • Horas Productivas Devueltas: +78.0 h a línea útil.    │
│ • Generar ahorro recurrente a Capex Cero (>$45k/año).   │ • Escape a Garantía: Reducido a < 1.00% con visión.     │
│ • Blindar la entrega reduciendo reclamos a < 1.00%.     ├─────────────────────────────────────────────────────────┤
├─────────────────────────────────────────────────────────┤ 7. ESTANDARIZACIÓN Y SEGUIMIENTO (STANDARDIZATION)     │
│ 4. ANÁLISIS CAUSA RAÍZ (ROOT CAUSE ANALYSIS)            │ • Procedimiento POE-CAL-04 actualizado y firmado.       │
│ • Ishikawa 4M: Velocidad forzada (>139 u/h) causa +49%  │ • Auditoría mensual de COPQ en reunión de operaciones.  │
│   defectos; máquinas >8 años elevan fallas 63%.         │ • Tablero Power BI desplegado para monitoreo gerencial. │
│ • 5 Porqués: La falta de un límite de severidad en piso │ • Capacitación One-Point Lesson a todos los turnos.     │
│   incentivaba el retrabajo a ciegas.                    │                                                         │
└─────────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────┘
```

---

## 1. Antecedentes y Justificación del Negocio
En el entorno de manufactura industrial de alta cadencia evaluado (10,000 eventos de producción auditados), la política no escrita de piso era "intentar recuperar todo lo posible". 

Esta práctica generaba un **desperdicio silencioso y masivo de recursos**: operarios dedicando horas de turno a reacondicionar piezas con fallas estructurales graves que, tras pasar por el banco de trabajo y consumir energía, no cumplían las pruebas finales de laboratorio y terminaban siendo destruidas como chatarra.

---

## 2. Condición Actual: Diagnóstico Cuantitativo del Problema

### El Costo de No Calidad (COPQ) Desglosado:
| Desenlace Operativo | Eventos Registrados | Costo Medio Unitario | Impacto Financiero en Planta |
|---|:---:|:---:|---|
| **1. Aprobado Directo** | 6,728 uds | **$23.54 USD** | Flujo ideal de producción conforme |
| **2. Retrabajo Exitoso** | 2,033 uds | **$36.67 USD** | Recuperación económica rentable |
| **3. Scrap Directo** | 57 uds | **$101.31 USD** | Pérdida de material contenida |
| **4. Retrabajo Fallido (Scrap)** | **191 uds** | **$126.78 USD** | **¡PEOR DECISIÓN: Material + Mano de obra + Energía!** |

### La Trampa del Retrabajo Severo:
* En **Severidad 1 (Leve):** La tasa de éxito de retrabajo es del **87.8%** y la tasa de scrap es **0.0%**. Retrabajar es rentable.
* En **Severidad 2 (Moderada):** La tasa de éxito es del **70.6%** y el scrap sube al **19.0%**. Rentabilidad condicional.
* En **Severidad 3 (Grave / Estructural):** La tasa de éxito cae a **48.3%** y el **31.5% va directamente a scrap**. Retrabajar cuesta $126.78 USD frente a $101.31 USD de scrap directo.

---

## 3. Objetivos Cuantificables del Proyecto (Metas SMART)
1. **Reducción de Pérdidas por Doble Costo:** Disminuir de 191 a 0 las piezas con Severidad 3 sometidas a retrabajo fallido en los próximos 30 días.
2. **Impacto Financiero:** Generar un ahorro recurrente de **+$48,784 USD/año** para la planta a Capex Cero.
3. **Productividad de Línea:** Recuperar **78 horas hombre de operarios** al mes para tareas productivas en lugar de reprocesos estériles.
4. **Calidad de Cliente:** Reducir la tasa de fuga de defectos a reclamo en garantía del **1.61% al < 1.00%**.

---

## 4. Análisis Causa Raíz (Ishikawa & 5 Porqués)

### Diagrama de Ishikawa (Espina de Pescado 4M):
```text
  MÁQUINAS                             MÉTODOS
  Activos con >8 años de servicio       Falta de criterio estándar de scrap
  Holguras en guías y mordazas         Inspección manual con fatiga visual (1.61% fuga)
            \                           /
             \                         /
              ---------> DEFECTOS Y --+---> SOBRECOSTO POR RETRABAJO FALLIDO
             /           DESPERDICIOS |
            /                         \
  Operación a >139 u/h (+49% defectos) Materia prima Grado C (+40% defectos)
  Presión por cumplir cuota de turno   Variabilidad de dureza de insumos
  MANO DE OBRA / OPERACIÓN             MATERIALES
```

### Los 5 Porqués de la Falla Operativa:
1. *¿Por qué el retrabajo fallido costó $126.78 USD por unidad?*  
   $\rightarrow$ Porque se gastaron horas de operario y energía en piezas que igual terminaron en chatarra.
2. *¿Por qué se autorizó retrabajar esas piezas?*  
   $\rightarrow$ Porque los supervisores intentaban salvar piezas con defectos estructurales graves (Severidad 3).
3. *¿Por qué intentaban salvarlas?*  
   $\rightarrow$ Porque el indicador de planta penalizaba el scrap inmediato del turno, pero no medía el costo acumulado de no calidad (COPQ).
4. *¿Por qué se generaban tantos defectos graves en primer lugar?*  
   $\rightarrow$ Porque las líneas se forzaban por encima de 139 u/h en máquinas antiguas de más de 8 años.
5. *¿Causa Raíz Sistémica?*  
   $\rightarrow$ **Falta de un límite operativo de velocidad para activos críticos y ausencia de un estándar visual de corte de retrabajo en la estación de inspección.**

---

## 5. Plan de Contramedidas Implementado (Acciones CAPA)

| ID | Contramedida | Tipo | Responsable | Estado |
|---|---|:---:|:---:|:---:|
| **CAPA-01** | **Regla de Corte en Severidad 3:** Prohibición formal de retrabajo en fisuras y defectos estructurales. Envío directo a scrap ($101.31 USD). | Procedimental | Angelo Apolo / QA | Implementado |
| **CAPA-02** | **One-Point Lesson (OPL) Plastificada:** Colocación de tabla visual de criterios y tolerancias en cada estación de control. | Visual / Piso | Supervisor de Línea | En estación |
| **CAPA-03** | **Enclavamiento de Velocidad en PLC:** Bloqueo de velocidad máxima a 125 u/h en máquinas con más de 6 años de antigüedad. | Técnico / Control | Mantenimiento / PLC | Calibrado |
| **CAPA-04** | **Priorización de Visión Artificial:** Despliegue de cámaras de inspección en puestos críticos para abatir el 1.61% de fuga manual. | Tecnología | Ingeniería de Procesos | Validado |

---

## 6. Confirmación de Efectos y Retorno Financiero

```text
       LÍNEA BASE (HISTÓRICO)                  ESTADO MEJORADO (CON A3)
  ┌───────────────────────────────┐       ┌───────────────────────────────┐
  │ Scrap Doble Costo: 191 piezas │       │ Scrap Doble Costo: 0 piezas   │
  │ Costo Unitario: $126.78 USD   │ ----> │ Costo Contenido: $101.31 USD  │
  │ Horas Perdidas: 78.0 h        │       │ Horas Devueltas: +78.0 h      │
  │ Fuga Garantía: 1.61% (Manual) │       │ Fuga Garantía: < 1.00%        │
  └───────────────────────────────┘       └───────────────────────────────┘
                     AHORRO NETO: +$48,784 USD / AÑO (Capex Cero)
```

---

## 7. Estandarización y Prevención de Recurrencia
1. **Procedimiento Operativo:** Se actualizó formalmente el **POE-CAL-04: Criterios de Aceptación, Reproceso y Descarte Directo**.
2. **Capacitación Operativa:** 100% de los supervisores e inspectores de los 3 turnos capacitados con la One-Point Lesson (OPL).
3. **Gobernanza:** Integración del Cuadro de Mando Power BI en la junta mensual de Operaciones y Dirección de Planta para control de tendencias de COPQ.
