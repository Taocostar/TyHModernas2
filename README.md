# 📷 Fotografía forense aplicada a la ingeniería: análisis de una pieza metálica soldada

Informe técnico que aplica técnicas de **fotografía forense** para el registro, análisis e interpretación de evidencias visuales en el ámbito de la ingeniería industrial. A partir de una serie de fotografías de una pieza de acero, se documenta qué se observa, se evalúan los parámetros técnicos de captura, se analiza el color y se formula una hipótesis fundada sobre el origen, el proceso y el estado del objeto.

> **Idea central:** una fotografía correctamente capturada, analizada y con metadatos íntegros puede funcionar como **prueba documental** y como base para la **toma de decisiones técnicas**.

---

## 🎯 Objetivos

- Registrar y describir una evidencia visual con criterio técnico.
- Analizar parámetros fotográficos: iluminación, exposición, profundidad de campo, enfoque, perspectiva y escala.
- Realizar un análisis cualitativo de color e interpretarlo desde la ingeniería de materiales (corrosión, soldadura, recubrimientos).
- Leer metadatos (EXIF) y establecer una cadena de custodia digital mediante hashes SHA-256.
- Formular hipótesis sobre el origen, el proceso de fabricación y el posible uso del objeto.
- Evaluar el valor probatorio de la serie y proponer mejoras para un registro de calidad pericial.

---

## 🔍 El objeto analizado

Conjunto de barras de **acero corrugado (hierro nervado)** cortadas a igual longitud, unidas por soldadura en un extremo y rematadas con una **tuerca hexagonal soldada a modo de ojal**. Lleva atado un **alambre plastificado naranja**.

| Característica | Detalle |
|---|---|
| Material probable | Acero al carbono laminado en caliente (tipo ADN 420) |
| Cantidad de barras | Al menos 3, probablemente 4 |
| Dimensiones estimadas | Largo ≈ 12–14 cm; diámetro de cada barra ≈ 20–30 mm (±25 %, sin escala métrica) |
| Unión | Soldadura (arco manual o MIG) con escoria y salpicaduras |
| Estado | Corrosión generalizada heterogénea, con depósitos gris-blanquecinos |

---

## 🗂️ Contenido del informe

1. **Ficha de identificación:** objeto, material de registro, fecha de los archivos, escenario y referencia de escala.
2. **Registro fotográfico:** las 7 tomas originales con su descripción.
3. **Metadatos y cadena de custodia digital:** inspección EXIF, tabla de archivos y hashes SHA-256.
4. **Análisis técnico fotográfico:**
   - Resumen cuantitativo por imagen (luminancia, contraste, nitidez).
   - Iluminación y exposición.
   - Profundidad de campo, enfoque y perspectiva.
   - Análisis de color por zonas.
5. **Descripción de lo observado.**
6. **Interpretación:** origen del material, proceso de transformación, posible uso en la industria y causas del estado actual.
7. **Evaluación de la serie como prueba documental.**
8. **Recomendaciones para un registro de calidad pericial.**
9. **Conclusión.**
10. **Anexo:** hashes SHA-256 completos.

---

## 🧪 Metodología

- **Inspección visual** de las 7 imágenes (1200 × 1600 px, JPEG, relación 3:4).
- **Lectura de metadatos** con Pillow y ExifTool.
- **Mediciones sobre los píxeles** con Python (Pillow, OpenCV, NumPy):
  - Luminancia media y contraste (desviación estándar).
  - Recorte de sombras y de altas luces.
  - Nitidez como varianza del Laplaciano en el área central del objeto.
  - Color medio en RGB y HSV por zona.
- **Integridad:** hash SHA-256 de cada archivo recibido.
- **Interpretación** basada en conocimientos de materiales, soldadura y corrosión.

---

## 📊 Principales resultados

- **Metadatos:** los 7 archivos **no contienen EXIF** (WhatsApp lo elimina al recomprimir). Por eso no se puede acreditar fecha, lugar ni dispositivo de captura.
- **Exposición:** histograma bien centrado (luminancia media 138–156), pero el fondo claro tiende a subexponer el objeto (fotos 1, 3 y 7).
- **Nitidez:** la foto 6 es la más nítida y la 3 la menos nítida. Las mejores tomas para análisis son la **5** (vista general) y la **7** (cenital con luz pareja).
- **Color:**
  - Marrón-anaranjado → óxidos e hidróxidos de hierro (corrosión atmosférica).
  - Parches gris-blanquecinos → restos de cemento o mortero, o sales.
  - Tuerca gris con polvo blanco → probable galvanizado con herrumbre blanca de zinc.
  - Manchas negras → escoria y salpicaduras de soldadura.
  - Alambre naranja → recubrimiento plástico, agregado posterior.
- **Interpretación:** pieza maciza, sin elementos activos, hecha con **sobrantes de acero de construcción**. Lo más probable es que sea una **pesa o contrapeso artesanal** o una **práctica de taller de soldadura**, expuesta a humedad durante semanas o meses.

> ⚠️ Las conclusiones sobre material, uso e historia son **hipótesis fundadas**, no resultados de ensayos de laboratorio.

---

## ✅ Valoración de la serie como evidencia

| Criterio | Valoración |
|---|---|
| Cobertura de ángulos | Buena |
| Nitidez y exposición | Aceptable a buena |
| Escala métrica | Deficiente |
| Color fiel | Deficiente |
| Metadatos y trazabilidad | Deficiente (se agregan hashes) |
| Contexto y ubicación | Parcial |

---

## 🛠️ Recomendaciones para un registro pericial

- Incluir **escala milimetrada** y **carta gris 18 % / carta de color** en cada toma.
- Usar **trípode**, modo manual, ISO bajo, apertura f/8–f/11 y **RAW + JPEG** con balance de blancos fijo.
- Iluminar con **luz difusa** para vistas generales y **luz rasante** para texturas; evitar el flash directo sobre metal.
- Seguir un orden de tomas: contexto → vista general con etiqueta → caras con escala → macros de soldadura, rosca y depósitos.
- Enviar los originales como **documento** (no como foto) para conservar el EXIF, y calcular el **hash** al capturar.
- Complementar con ensayos: pesaje, calibre, imán, dureza, **XRF** de los depósitos y metalografía de la soldadura.



## ✍️ Autoría

Trabajo realizado en el marco del taller de **fotografía forense aplicada a la ingeniería**.
Autor/a: ALIAGA Tomas, COSTARELLI Bernardo, LA MOTTA Franco, MATALONI Sabrina, SIRACUSA Juan Pablo
````
