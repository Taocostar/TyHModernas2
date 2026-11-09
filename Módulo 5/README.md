# TP 5 · Dinámica de Sistemas: retroalimentación con flujos constantes

**Técnicas y Herramientas Modernas 2** · Ingeniería Industrial (5.º año)

## Integrantes

Franco LaMotta · Bernardo Costarelli · Tomás Aliaga · Juan Pablo Siracusa · Sabrina Mataloni

## De qué trata

Este trabajo estudia cómo se comporta un sistema con **un solo stock** y **retroalimentación** cuando además tiene **flujos constantes** (una entrada o una salida fija). La conclusión central es que un flujo constante no cambia el tipo de comportamiento ni la constante de tiempo del sistema: solo **desplaza el equilibrio**.

Se trabajan cuatro casos, tomados de documentos del *MIT System Dynamics in Education Project*:

| Caso | Estructura | Equilibrio |
|---|---|---|
| Moscas de la fruta | Realimentación positiva + salida constante | 100 moscas |
| Fondo del Premio Nobel | Realimentación positiva + salida constante | USD 60 millones |
| Lavabo con goteo | Realimentación negativa + entrada constante | 300 cm³ |
| Memorización de letras | Realimentación negativa + entrada constante | 45 palabras (aria) |

El método es la **simulación mental** en tres pasos: calcular el equilibrio, determinar el modo de comportamiento y graficar. Los resultados se verifican con una simulación (Vensim o el script de Python incluido).

## Contenido del repositorio

```
.
├── README.md
├── informe/
│   └── informe.md                  # Teoría, casos, guía de Vensim y resultados
├── presentacion/
│   └── Dinamica_de_Sistemas_Flujos_constantes.pptx
├── simulacion/
│   ├── simulacion.py               # Replica los modelos (Euler, paso 0,0625)
│   ├── requirements.txt
│   └── figuras/                    # Gráficos generados
└── material-fuente/                # Documentos originales del MIT
    ├── D-4546-2_Mental_Simulation_Adding_Constant_Flows.pdf
    └── D-4596_Graphical_Integration_Part_3_Combined_Flows.pdf
```

## Cómo empezar

1. Leer el [informe](informe/informe.md). Tiene la teoría, la resolución de los ejercicios y el paso a paso para armar los modelos en Vensim.
2. Ver la presentación en [`presentacion/`](presentacion).
3. Reproducir los gráficos:

```bash
cd simulacion
pip install -r requirements.txt
python simulacion.py
```

El script imprime en consola la comparación entre el valor simulado y el analítico, y guarda los gráficos en `simulacion/figuras/`.

## Simulación en Vensim

Los modelos se arman en **Vensim PLE**, gratuito para uso educativo y personal: [vensim.com/free-download](https://vensim.com/free-download/). La sección 5 del [informe](informe/informe.md#5-simulación-en-vensim-cómo-hacerla) incluye el diagrama a dibujar, las ecuaciones de los cuatro modelos y una lista de experimentos para probar.

## Fuentes y atribución

- Coronado, A. E. (1996). *Beginner Modeling Exercises, Section 4: Mental Simulation: Adding Constant Flows* (D-4546-2). MIT System Dynamics in Education Project.
- Agatstein, K. y Breierova, L. (1996). *Graphical Integration Exercises, Part Three: Combined Flows* (D-4596). MIT System Dynamics in Education Project.

Los documentos del MIT indican que se permite copiarlos con fines educativos no comerciales. Se incluyen en `material-fuente/` solo como material de consulta; los derechos pertenecen al MIT.

## Flujo de trabajo del equipo

- Una rama por cambio (`informe-vensim`, `fix-figuras`, etc.) y *pull request* hacia `main`.
- Mensajes de commit descriptivos, por ejemplo: `Agrega ecuaciones del modelo de lavabo`.
- No subir archivos temporales ni versiones duplicadas de la presentación.
