# 🎨 Guía de Diseño Visual y Maquetación: Dashboard Power BI
## Especificación UI/UX para Presentación Ejecutiva de Calidad y COPQ
**Proyecto 03 | Portafolio Técnico de Operaciones y Calidad Industrial**  
**Autor:** Angelo Apolo | Especialista en Aseguramiento de Calidad & Six Sigma  

---

## 🎯 1. Paleta de Colores Corporativa (Design System)

| Elemento UI | Nombre del Tono | Código Hex | Uso en el Tablero |
|---|---|:---:|---|
| **Cabecera & Títulos** | Azul Marino Industrial | `#1B365D` | Banner superior, títulos de página y métricas principales |
| **Lienzo / Fondo** | Gris Ejecutivo Suave | `#F4F6F9` | Fondo general de la página para evitar fatiga visual |
| **Tarjetas KPI** | Blanco Puro | `#FFFFFF` | Contenedores con sombra suave (*Drop Shadow*) y esquinas redondeadas (12px) |
| **Aprobado / Éxito** | Verde Esmeralda | `#2ECC71` | Piezas conformes y ahorros netos positivos |
| **Retrabajo Aceptable** | Azul Acero | `#3498DB` | Reprocesos exitosos y sensores ópticos |
| **Scrap Directo** | Naranja Alerta | `#E67E22` | Chatarra contenida a costo estándar ($101.31 USD) |
| **Retrabajo Fallido** | Rojo Crítico | `#C0392B` | Pérdida doble ($126.78 USD) - Destacado en rojo de advertencia |
| **Fuga Manual** | Ámbar Advertencia | `#D35400` | Barra de escape a garantía en inspección manual (1.61%) |

---

## 🖼️ 2. Modelos Visuales de Referencia (Página por Página)

### Página 1: Resumen Ejecutivo de Calidad & COPQ
* **Objetivo:** Vista para el Director de Planta y Gerencia de Operaciones.
* **Composición:**
  * **Header Superior:** Banner azul marino `#1B365D` con título formal y segmentadores de *Planta*, *Línea* y *Turno*.
  * **Fila Superior (5 Tarjetas KPI):** `COPQ Total ($48.8K)`, `Tasa Scrap % (2.5%)`, `Tasa Retrabajo % (24.3%)`, `Reclamos Garantía 90d (125)`, `Ahorro Anual Proyectado (+$48,784 USD)`.
  * **Visual Inferior Izquierdo:** Gráfico de columnas de *Costo Medio por Desenlace Operativo*, destacando en rojo el salto de costo a **$126.78 USD** en retrabajo fallido.
  * **Visual Inferior Derecho:** Gráfico de anillo (*Donut Chart*) con el desglose del COPQ entre *Falla Interna Scrap*, *Falla Interna Retrabajo* y *Falla Externa Garantía*.

---

### Página 2: Análisis Causa Raíz & Desempeño Operativo
* **Objetivo:** Vista técnica para Comités de Mejora Continua y Six Sigma.
* **Composición:**
  * **Fila Superior (4 Tarjetas KPI):** `Unidades Scrap (248)`, `Unidades Retrabajadas (2,434)`, `Éxito de Retrabajo % (70.6%)`, `Pérdida Retrabajo Fallido ($4.8K)`.
  * **Visual Izquierdo:** Diagrama de Pareto 80/20 de tipos de defectos (`Dimension`, `Finish`, `Contamination`, `Crack`, `Scratch`) con curva roja de porcentaje acumulado.
  * **Visual Superior Derecho:** Gráfico de barras comparando la *Tasa de Defectos por Velocidad de Línea* (Normal 14.8% vs. Forzada >139 u/h a 19.2%).
  * **Visual Inferior Derecho:** Gráfico de barras horizontales mostrando la degradación de calidad por *Antigüedad del Activo* (<4 años a 12.2% vs. >8 años a 19.9%).

---

### Página 3: Eficacia de Inspección & Blindaje ante Cliente
* **Objetivo:** Vista de Aseguramiento de Calidad (QA/QC) y relación con clientes.
* **Composición:**
  * **Fila Superior (3 Tarjetas KPI):** `Total Eventos (10,000)`, `Reclamos de Garantía 90d (125)`, `Tasa de Escape a Cliente (1.25%)`.
  * **Visual Izquierdo:** Gráfico de barras horizontales comparando la *Tasa de Escape a Garantía por Método de Inspección*, destacando la inspección manual en ámbar (1.61%) frente a sensores (0.93%) y visión artificial (1.05%).
  * **Visual Derecho:** Gráfico de anillo (*Donut Chart*) mostrando los *Reclamos en Garantía según Grado de Materia Prima* (Grado A 35%, Grado B 45%, Grado C 20%).

---

## 🛠️ 3. Pasos para Aplicar este Estilo en Power BI Desktop

1. **Fondo del Lienzo (Canvas Background):**
   * En el panel de Formato del lienzo -> *Fondo del lienzo* -> Color: `#F4F6F9`, Transparencia: `0%`.
2. **Contenedores de Tarjetas KPI:**
   * Fondo: `#FFFFFF`.
   * Borde visual: activado con radio de esquina de `12 px`.
   * Sombra (*Drop Shadow*): activada con desplazamiento exterior inferior derecho, color gris suave.
3. **Colores de Datos en Gráficos:**
   * En el gráfico de desenlace operativo, asigna manualmente el color `#C0392B` a la columna *Retrabajo Fallido (Scrap)* y `#2ECC71` a *Aprobado Directo*.
4. **Banner Superior:**
   * Inserta una forma rectangular en la parte superior (alto 75 px, ancho 1280 px), color de relleno `#1B365D`, sin borde, y coloca el cuadro de texto con letra blanca en fuente *Segoe UI Semibold*.
