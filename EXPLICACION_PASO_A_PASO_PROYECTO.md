# 🎯 Guía Maestra para Entrevistas Laborales: Control de Calidad, Scrap y Retrabajo
## Cómo Vender este Proyecto ante Gerentes de Planta, Directores de Operaciones y Jefes de Calidad
**Candidato:** Angelo Apolo | Ing. Químico / Industrial | Máster en Dirección de Proyectos  
**Target:** Jefe / Ingeniero de Aseguramiento de Calidad (QA/QC), Ingeniero de Procesos / Six Sigma, Coordinador de Planta  

---

## ⏱️ 1. Tu Historia en 30 Segundos (Elevator Pitch)
> *"En planta, el dilema diario del inspector es: **¿reproceso la pieza con defecto o la mando directo a la basura (scrap)?**  
> Muchas veces 'repararla' parece económico, pero si el defecto es severo, más del 50% de las piezas igual fracasan, terminando en la chatarra con un costo acumulado de **$126.78 USD** frente a los $101.31 USD del descarte inmediato.  
> Con 10,000 eventos reales de producción diseñé un **Semáforo de Decisión en Piso**: una herramienta visual que en 5 segundos predice la viabilidad técnica y calcula el beneficio financiero antes de tocar la pieza. Eliminamos 191 eventos de doble pérdida, liberamos 78 horas hombre y proyectamos un ahorro de más de **$48,000 USD al año a Capex Cero**."*

---

## 🎙️ 2. Tu Historia en 2 Minutos (Respuesta Estructurada STAR)

* **Situación:** *"En la planta evaluada se procesaban miles de unidades por turno y el 24.3% de las piezas se desviaba a reproceso bajo criterios subjetivos de cada supervisor. Descubrí que 191 piezas retrabajadas terminaban siendo destruidas de todas formas, duplicando las pérdidas."*
* **Tarea:** *"Mi objetivo como líder de aseguramiento de calidad fue erradicar el retrabajo a ciegas, diseñar una regla objetiva de decisión y blindar la planta ante fugas a garantía."*
* **Acción:** *"Apliqué la metodología Six Sigma DMAIC. Con estadística inferencial identifiqué los 3 detonantes físicos de defectos: forzar la velocidad de línea (+49% defectos), desgaste en máquinas de más de 8 años (+63% defectos) y materias primas Grado C. Luego entrené un modelo logístico de probabilidad de éxito ($P \ge 75\%$ = Retrabajar, $P < 55\%$ = Scrap Directo) y lo empaqueté en dos herramientas de piso: una plantilla Excel interactiva de 1 sola página para el supervisor y un dashboard web con semáforo en vivo."*
* **Resultado:** *"Erradicamos el 100% de las piezas en la zona de doble costo ($126.78 USD), generamos un ahorro directo de $4,864 USD en la muestra ($48,648 USD anualizados), devolvimos 78 horas productivas a las líneas y bajamos el riesgo de reclamos de clientes en garantía."*

---

## 📊 3. Los 3 Únicos Números que Debes Memorizar
Si te quedas en blanco en una entrevista, solo recuerda estas 3 cifras:
1. **$126.78 USD vs. $101.31 USD:** Es el costo de retrabajar una pieza que igual termina en scrap frente al descarte directo. Cada vez que el semáforo frena un retrabajo inviable, la planta ahorra **$25.47 USD netos**.
2. **51.7% de fracaso en Severidad 3:** Los defectos graves (grietas o fisuras estructurales) no se recuperan con pulido ni ajuste en línea. Retrabajarlos es tirar dinero bueno sobre dinero malo.
3. **+78 Horas devueltas y +$48,000 USD/año:** El beneficio operativo y financiero tangible a Capex Cero.

---

## 🧠 4. Las 7 Preguntas Más Difíciles de Entrevista y Cómo Responderlas

### Pregunta 1: "¿Por qué mandar a scrap directo si un buen operario tal vez podría salvar la pieza?"
* **Respuesta Ganadora:**  
  *"En manufactura no podemos gestionar por optimismo sino por estadística y costo esperado. En la Severidad 3 comprobamos que el 51.7% de las piezas no pasan la prueba final y el 31.5% terminan en scrap. Eso significa que la empresa paga el costo de la pieza, más 24 minutos de sueldo del operario, más energía eléctrica, solo para terminar botándola. Cuando la probabilidad de éxito es menor al 55%, el valor monetario esperado del retrabajo es negativo. El verdadero aseguramiento de calidad consiste en saber cuándo cortar la pérdida a tiempo."*

### Pregunta 2: "¿Cómo calculaste el ahorro de $48,000 USD al año?"
* **Respuesta Ganadora:**  
  *"En la muestra de 10,000 eventos registramos exactamente 191 piezas que sufrieron retrabajo fallido. La diferencia de costo entre el retrabajo fallido ($126.78 USD) y el scrap directo ($101.31 USD) es de $25.47 USD por pieza. Multiplicado por las 191 piezas da un ahorro neto auditado de $4,863.79 USD. En una operación continua de 100,000 eventos anuales (típica de 2 líneas en 3 turnos), la proyección directa a volumen anualizado supera los $48,000 USD netos, sin comprar maquinaria nueva."*

### Pregunta 3: "¿Cómo reaccionaron los supervisores de piso? A la gente no le gusta que le impongan sistemas."
* **Respuesta Ganadora:**  
  *"Por eso no les entregué un software complejo ni un manual de 50 páginas. Les diseñé una plantilla Excel de 1 sola página que abre en cualquier computadora de línea y un simulador web con 4 casillas. El supervisor solo marca el tipo de defecto y la severidad, y la celda se pinta automáticamente en Verde, Amarillo o Rojo. Al mostrarles que la herramienta los protegía de ser cuestionados a fin de mes por costos de scrap oculto, la adoptaron de inmediato."*

### Pregunta 4: "¿Qué descubriste sobre los métodos de inspección (Manual vs. Sensores vs. Visión)?"
* **Respuesta Ganadora:**  
  *"Analicé la tasa de reclamos de clientes en garantía a 90 días (`warranty_claim_90d`). La inspección manual tuvo una tasa de fuga a cliente de 1.61%, mientras que la visión artificial y sensores ópticos la mantuvieron cerca del 1.00%. La inspección manual tiene un 70% más de riesgo de escape de defectos por fatiga visual del inspector. La recomendación fue migrar los puntos de inspección de piezas críticas a visión artificial."*

### Pregunta 5: "¿Cómo se relaciona este proyecto con tu experiencia previa en laboratorio y planta?"
* **Respuesta Ganadora:**  
  *"En mis roles previos en empresas como Incarpalm y Agua Azul trabajé directamente en muestreo, inspección fisicoquímica y aseguramiento de especificaciones bajo normas técnicas. Sé perfectamente que en piso existe la tentación de 'darle una segunda pasada' a un lote dudoso. Lo que aporta este proyecto es mi visión de Dirección de Proyectos y Six Sigma: convertir la intuición empírica en una regla financiera y estadística medible."*

### Pregunta 6: "¿Qué variables de proceso fueron las verdaderas causas raíz de los defectos?"
* **Respuesta Ganadora:**  
  *"Aislé 3 factores determinantes:  
  1. **Velocidad de proceso:** Cuando los turnos forzaban la máquina a más de 139 u/h para recuperar tiempo, la tasa de defectos subía de 12.9% a 19.2% (+49%).  
  2. **Antigüedad de máquina:** Activos con más de 8 años duplicaban la tasa de defectos frente a activos nuevos por fatiga y desgaste mecánico.  
  3. **Materia prima:** El insumo Grado C generaba un 40% más de defectos que el Grado A.  
  La solución no fue solo inspeccionar mejor, sino emitir un protocolo CAPA 8D para limitar la velocidad a 125 u/h en máquinas antiguas."*

### Pregunta 7: "¿Qué pasa si una pieza está en color Amarillo (Zona de Evaluación)?"
* **Respuesta Ganadora:**  
  *"La zona amarilla corresponde a probabilidades de éxito entre el 55% y el 75% (típicamente Severidad 2 en defectos como descalibración o acabado). La regla estandarizada es: solo se autoriza retrabajo si la máquina opera a velocidad nominal y si la orden no pertenece a un cliente con penalizaciones contractuales por tiempo de entrega. De lo contrario, se descarta."*

---

## 🛠️ 5. Resumen de Entregables Disponibles en tu Portafolio
1. **Semáforo Interactivo Web (`server.py`):** Demostración interactiva en vivo lista para proyectar en una pantalla de entrevista.
2. **Matriz Excel de Piso (`Matriz_Decision_Retrabajo_Piso.xlsx`):** Plantilla interactiva con formato condicional y fórmulas automatizadas.
3. **Ficha Ejecutiva STAR (`Ficha_Ejecutiva_STAR_Proyecto.md`):** Hoja resumen para adjuntar a postulaciones ejecutivas.
4. **Protocolo CAPA 8D (`Protocolo_CAPA_8D_Visual.md`):** Evidencia documental de cierre de causa raíz bajo estándares automotrices / industriales.
5. **Notebook Ejecutivo (`01_control_calidad_copq_y_decision.ipynb`):** Código limpio y reproducible con gráficos ejecutivos de decisión.
