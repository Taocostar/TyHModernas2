# Análisis geoespacial con QGIS: superficie de cebolla y cobertura de nieve

Repositorio con la documentación y los procedimientos de dos aplicaciones de análisis geoespacial realizadas con QGIS: la estimación de superficie cultivada con cebolla en General Alvear (Mendoza) y la comparación de la superficie cubierta por nieve en un sector de la cordillera de los Andes entre dos fechas.

## Tabla de contenidos

- [¿Qué es un SIG?](#qué-es-un-sig)
- [¿Qué es QGIS?](#qué-es-qgis)
- [¿Para qué sirve?](#para-qué-sirve)
- [Aplicaciones en este repositorio](#aplicaciones-en-este-repositorio)
- [Herramientas y sistema de referencia](#herramientas-y-sistema-de-referencia)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Limitaciones](#limitaciones)
- [Autores y licencia](#autores-y-licencia)

## ¿Qué es un SIG?

Un **Sistema de Información Geográfica (SIG)** es un conjunto de herramientas informáticas para capturar, almacenar, gestionar, analizar y representar datos con referencia espacial. Cada dato se asocia a una ubicación sobre la superficie terrestre, lo que permite cruzar información de distintas fuentes y responder preguntas del tipo *dónde*, *cuánto* y *cómo cambió*.

Un SIG trabaja con dos modelos de datos principales:

- **Vectorial:** puntos, líneas y polígonos con atributos asociados (por ejemplo, un lote de cultivo o un punto de interés).
- **Ráster:** matrices de píxeles con un valor por celda (por ejemplo, imágenes satelitales o modelos de elevación).

## ¿Qué es QGIS?

**QGIS** es un SIG de código abierto y gratuito, multiplataforma (Windows, macOS y Linux), publicado bajo licencia GNU GPL y mantenido por una comunidad internacional de desarrolladores y usuarios. Sitio oficial: <https://www.qgis.org>.

Sus características principales son:

- Soporte de numerosos formatos vectoriales y ráster, y de bases de datos espaciales.
- Gestión de sistemas de referencia de coordenadas y reproyección de capas.
- Herramientas de geoprocesamiento (recorte, buffer, unión, análisis ráster).
- Calculadora ráster y calculadora de campos para operar sobre los datos.
- Georreferenciación de imágenes mediante puntos de control.
- Ampliación mediante complementos (*plugins*) y automatización con Python (PyQGIS).
- Diseño de mapas e impresión de salidas cartográficas.

## ¿Para qué sirve?

Entre sus usos más comunes se encuentran:

- Cartografía y diseño de mapas temáticos.
- Teledetección: clasificación de coberturas del suelo, cálculo de índices y detección de cambios.
- Estimación de superficies y análisis de uso del suelo, agricultura y recursos naturales.
- Planificación territorial, logística y localización de instalaciones.
- Gestión de recursos hídricos, glaciares y riesgos naturales.

## Aplicaciones en este repositorio

### 1. Estimación de la superficie plantada con cebolla

En el marco de un proyecto final de ingeniería sobre la reingeniería de un secadero de ciruelas para la deshidratación de cebolla, con base en General Alvear (Mendoza), se utilizó QGIS para estimar las hectáreas plantadas con cebolla en el departamento y sus alrededores, dato necesario para dimensionar la disponibilidad de materia prima.

Procedimiento resumido:

1. Obtención de una escena Sentinel-2 nivel L2A (reflectancia de superficie) de la zona.
2. Digitalización de 16 polígonos de cultivos de cebolla como áreas de referencia.
3. Clasificación de la imagen, simplificando el criterio al considerar cebolla todo píxel con firma de vegetación verde.
4. Cálculo del área clasificada en hectáreas con el sistema de referencia proyectado.

Resultado: superficie estimada de **[completar] ha**.

### 2. Comparación de la superficie cubierta por nieve (2023 y actual)

Se estimó el área nevada de un sector de la cordillera de los Andes en dos momentos: una imagen georreferenciada de 2023 y una captura de Google Maps de noviembre de 2026.

Procedimiento resumido:

1. **Georreferenciación** de la captura con 6 puntos de control, transformación afín y remuestreo por vecino más cercano. El ajuste tuvo un RMSE de aproximadamente 2,3 píxeles (80 a 90 m).
2. **Región de interés:** polígono delimitado por los puntos clave del vuelo.
3. **Recorte** de cada ráster con el polígono como máscara.
4. **Clasificación por umbral de color RGB** en la Calculadora ráster, calibrando el umbral en cada imagen (salida binaria: 1 nieve, 0 no nieve).
5. **Reproyección** a EPSG:32719 con vecino más cercano y cálculo de áreas con el informe de valores únicos de capa ráster.

Resultados:

| | 2023 | Actual |
|---|---:|---:|
| Área de nieve (km²) | 12,53 | 12,32 |
| Variación | | −0,22 km² (−1,75 %) |

La diferencia es menor que la incertidumbre del método (error de georreferenciación, diferencia de resolución, umbrales distintos y mosaico de fechas en la captura de Google Maps), por lo que **no es concluyente**.

## Herramientas y sistema de referencia

| Elemento | Detalle |
|---|---|
| Software | QGIS 3.x |
| Sistema de referencia de trabajo | EPSG:32719 (WGS 84 / UTM zona 19S) |
| Datos de entrada | Imágenes satelitales (Sentinel-2 L2A), imagen aérea 2023, captura de Google Maps |
| Formato de salida | GeoTIFF y GeoPackage |
| Informe | LaTeX (Overleaf) |

## Estructura del repositorio

```text
.
├── README.md
├── informe/            # Informe en LaTeX (main.tex y figuras)
├── cebolla/            # Proyecto QGIS y salidas de la estimación de cebolla
├── nieve/              # Proyecto QGIS, rásters binarios y capas de la región
└── docs/               # Capturas y documentación adicional
```

## Limitaciones

- La clasificación por umbral de color sobre imágenes RGB es sensible a la iluminación, las sombras, las nubes y las etiquetas de la imagen.
- La clasificación de cebolla se realizó con una sola fecha, sin series temporales, lo que limita la separación entre cultivos.
- Las capturas de Google Maps no tienen fecha única ni metadatos radiométricos, por lo que no son adecuadas para mediciones de precisión.
- Para resultados defendibles se recomienda usar imágenes multiespectrales de la misma época del año y, para nieve, el índice NDSI.

## Autores y licencia

- Autor: Juan Bernardo Costarelli
- Institución: Universidad Nacional de Cuyo, Facultad de Ingeniería
