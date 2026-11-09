# Retroalimentación con flujos constantes

**Simulación mental y simulación en Vensim de sistemas de primer orden**

Técnicas y Herramientas Modernas 2 · Ingeniería Industrial (5.º año) · TP 5

**Integrantes:** Franco LaMotta · Bernardo Costarelli · Tomás Aliaga · Juan Pablo Siracusa · Sabrina Mataloni

> Este informe acompaña la presentación de la carpeta [`presentacion/`](../presentacion). Desarrolla la teoría con más detalle, explica cómo llevar los modelos a Vensim y presenta los resultados de la simulación, que se pueden reproducir con el script de [`simulacion/`](../simulacion).

---

## Índice

1. [Introducción y objetivos](#1-introducción-y-objetivos)
2. [Marco teórico](#2-marco-teórico)
3. [Casos de aplicación](#3-casos-de-aplicación)
4. [Integración gráfica de flujos combinados](#4-integración-gráfica-de-flujos-combinados)
5. [Simulación en Vensim: cómo hacerla](#5-simulación-en-vensim-cómo-hacerla)
6. [Resultados de la simulación](#6-resultados-de-la-simulación)
7. [Realimentación positiva vs. negativa y aplicación en Ingeniería Industrial](#7-realimentación-positiva-vs-negativa-y-aplicación-en-ingeniería-industrial)
8. [Conclusiones](#8-conclusiones)
9. [Bibliografía](#9-bibliografía)

---

## 1. Introducción y objetivos

La **Dinámica de Sistemas**, desarrollada por Jay W. Forrester en el MIT, parte de una idea: el comportamiento de un sistema a lo largo del tiempo (crecer, estabilizarse, oscilar, colapsar) lo genera su **estructura**, es decir, cómo se conectan sus acumulaciones, sus flujos y sus bucles de retroalimentación.

Para entender esa relación hay dos herramientas complementarias:

- la **simulación por computadora** (por ejemplo, con Vensim o Stella);
- la **simulación mental**: anticipar a mano, con cuentas simples y un boceto, qué va a hacer el sistema.

Este trabajo se basa en dos documentos del *MIT System Dynamics in Education Project*:

| Documento | Tema |
|---|---|
| D-4546-2, *Mental Simulation: Adding Constant Flows* (Coronado, 1996) | Simulación mental de sistemas de un solo stock con flujos constantes |
| D-4596, *Graphical Integration Exercises, Part Three: Combined Flows* (Agatstein y Breierova, 1996) | Cómo obtener el comportamiento de un stock a partir de sus flujos de entrada y salida |

**Objetivos**

1. Explicar cómo un flujo constante modifica el comportamiento de un sistema con retroalimentación positiva o negativa.
2. Aplicar el procedimiento de tres pasos de la simulación mental a los casos del documento.
3. Replicar los modelos en un software de simulación (Vensim) y validar los resultados contra el cálculo manual.
4. Relacionar los conceptos con problemas de la ingeniería industrial.

---

## 2. Marco teórico

### 2.1 Elementos básicos

| Concepto | Definición | Ejemplo |
|---|---|---|
| **Stock** (nivel) | Acumulación de algo en un instante. Solo cambia por sus flujos. | Población de moscas, saldo de una cuenta, agua en un lavabo, inventario |
| **Flujo** | Cantidad que entra o sale del stock por unidad de tiempo. | Reproducción, retiro de moscas, interés, premios |
| **Retroalimentación** | El stock influye sobre alguno de sus propios flujos. | Más moscas → más reproducción |

La ecuación fundamental de cualquier stock es:

```
Stock(t + dt) = Stock(t) + (Entradas − Salidas) · dt
```

o, en forma continua, `dS/dt = Entradas − Salidas`. Programas como Vensim resuelven exactamente esta integración paso a paso (método de Euler).

Hay dos tipos de bucles:

- **Positivo (de refuerzo):** amplifica los cambios. Más stock genera más flujo de entrada, que genera más stock. Produce crecimiento exponencial (o caída exponencial, si el stock está por debajo del punto de equilibrio).
- **Negativo (de equilibrio):** busca una meta. Más stock genera más flujo de salida, que reduce el stock. Produce convergencia hacia un valor.

### 2.2 Equilibrio de un sistema de primer orden

Un sistema de primer orden tiene un solo stock. Está en **equilibrio** cuando el stock no cambia, es decir, cuando

```
Suma de entradas = Suma de salidas
```

Sin flujos constantes, el equilibrio de estos sistemas está en cero (un lavabo sin goteo termina vacío). **Agregar un flujo constante desplaza el equilibrio** de cero a otro valor, que se calcula igualando entradas y salidas.

### 2.3 Realimentación positiva con salida constante

Es la estructura de las **moscas de la fruta** y del **Fondo Nobel**.

```
dS/dt = k · S − c          k = razón de crecimiento (1/tiempo)
                           c = salida constante (unidades/tiempo)
```

- **Equilibrio:** `k · S* = c`, entonces `S* = c / k`.
- **Desvío respecto del equilibrio:** si `d = S − S*`, entonces `dd/dt = k · d`, y la solución es `d(t) = d(0) · e^(k·t)`.

Esto dice tres cosas importantes:

1. La salida constante **no cambia la forma exponencial**: la constante de tiempo sigue siendo `1/k`.
2. Lo único que se amplifica es la **brecha** respecto del equilibrio, no el stock completo.
3. El equilibrio es **inestable**: si el stock está apenas por encima de `S*` crece sin límite; si está apenas por debajo, cae hasta agotarse.

### 2.4 Realimentación negativa con entrada constante

Es la estructura del **lavabo con goteo** y de la **memorización de letras**.

```
dS/dt = c − S / τ          c = entrada constante (unidades/tiempo)
                           τ = tiempo característico (1/fracción de salida)
```

- **Equilibrio:** `c = S*/τ`, entonces `S* = c · τ`.
- **Desvío:** `d(t) = d(0) · e^(−t/τ)`.

Acá el equilibrio es **estable**: arriba o abajo de `S*`, el stock converge hacia él. La entrada constante cambia la **meta** del sistema (de 0 a `c · τ`) pero no la velocidad con que se alcanza.

### 2.5 Resumen comparativo

| | Positiva + salida constante | Negativa + entrada constante |
|---|---|---|
| Ecuación | `dS/dt = k·S − c` | `dS/dt = c − S/τ` |
| Equilibrio `S*` | `c / k` | `c · τ` |
| Desvío `d = S − S*` | `d(0)·e^(k·t)` | `d(0)·e^(−t/τ)` |
| Estabilidad | Inestable (se aleja) | Estable (converge) |
| Tiempo característico | Tiempo de duplicación | Vida media |
| Efecto del flujo constante | Desplaza el equilibrio | Desplaza el equilibrio |
| Efecto sobre la constante de tiempo | Ninguno | Ninguno |

### 2.6 Tiempo de duplicación y vida media

Para estimar curvas rápido se usan dos atajos:

```
Tiempo de duplicación = ln 2 / k  ≈ 0,7 / k        (realimentación positiva)
Vida media            = τ · ln 2  ≈ 0,7 · τ         (realimentación negativa, τ = 1/fracción)
```

El valor exacto de `ln 2` es 0,693; la aproximación 0,7 alcanza para un boceto. En los ejemplos: moscas, 0,7 / 0,5 = 1,4 días; Fondo Nobel, 0,7 / 0,10 = 7 años; lavabo, 0,7 / 0,1 = 7 segundos.

### 2.7 Superposición

Estos sistemas son **lineales**, así que el comportamiento total se puede obtener sumando dos comportamientos por separado:

1. la parte del stock que está **en equilibrio** (una línea horizontal en `S*`);
2. la parte del stock que está **fuera de equilibrio** (la curva exponencial del desvío).

Graficar el sistema completo equivale a **tomar la curva exponencial y desplazarla verticalmente hasta que parta de `S*`**. La superposición solo es válida en sistemas lineales; con no linealidades hay que simular.

### 2.8 Procedimiento de simulación mental (tres pasos)

| Paso | Qué se hace | Cómo |
|---|---|---|
| **1. Calcular el equilibrio** | Igualar entradas y salidas | `Σ entradas = Σ salidas` |
| **2. Determinar el modo de comportamiento** | Comparar el stock inicial con el equilibrio | Igual: equilibrio. Distinto: se aleja (positiva) o converge (negativa) |
| **3. Graficar** | Sumar equilibrio y exponencial | Línea en `S*` + curva del desvío usando duplicación o vida media |

---

## 3. Casos de aplicación

### 3.1 Moscas de la fruta (positiva + salida constante)

Un científico cría moscas con una razón de reproducción de 50 % por día y retira 50 moscas por día.

- **Paso 1:** `Población · 0,5 = 50` → equilibrio = **100 moscas**.
- **Paso 2:** con 100 moscas, el modo es equilibrio.
- **Si llegan 120 moscas:** las 100 que están en equilibrio se mantienen y las **20 extra** crecen exponencialmente, duplicándose cada 1,4 días.

| Día | 0 | 1,4 | 2,8 | 4,2 |
|---|---|---|---|---|
| Moscas extra | 20 | 40 | 80 | 160 |
| **Población total** | **120** | **140** | **180** | **260** |

*Aclaración útil:* las 120 moscas **no** se duplican en 1,4 días. El tiempo de duplicación se aplica solo al excedente de 20, porque las otras 100 se retiran al mismo ritmo al que se reproducen.

### 3.2 Fondo del Premio Nobel (positiva + salida constante)

La Fundación entrega unos USD 6.000.000 por año en premios, financiados con los intereses de una cuenta al 10 % anual.

**A. Modelo con seis salidas.** Un stock (Fondo), un flujo de entrada (interés = Fondo × tasa, bucle positivo) y seis flujos de salida constantes, uno por premio: Química, Literatura, Medicina, Física, Economía y Paz.

**B. Modelo con una salida agregada.** Los seis premios se suman en un solo flujo de USD 6 M/año. El comportamiento es idéntico y el modelo es más simple: agregar variables cuando es posible simplifica el modelo sin cambiar el comportamiento que se observa.

**C. Saldo mínimo.**

```
Interés = Premios  →  Fondo · 0,10 = 6.000.000  →  Fondo = USD 60.000.000
```

Con USD 60 M, el interés anual paga exactamente los premios y el fondo se mantiene indefinidamente. Coincide con la fórmula de **perpetuidad** de la ingeniería económica: capital necesario = pago periódico / tasa.

**D. Fondo inicial de USD 30 M.**

1. Equilibrio: USD 60 M.
2. Modo: 30 < 60, así que el déficit crece exponencialmente y el fondo se aleja del equilibrio hacia abajo.
3. Gráfico: el déficit pasa de −30 M a −60 M en 7 años (tiempo de duplicación), por lo que el fondo vale `60 − 60 = 0` en ≈ 7 años. Con el cálculo exacto, `Fondo(t) = 60 − 30·e^(0,1·t)` se anula en `t = ln 2 / 0,1 = 6,93` años.

*Limitación del modelo:* deja que el saldo sea negativo (−39,6 M a los 12 años). En la realidad ningún banco admitiría esa cuenta, y la Fundación reduciría premios o agregaría fondos.

**E. Premio de Dinámica de Sistemas.** Con USD 60,5 M en el fondo, el excedente sobre el equilibrio es USD 0,5 M. Solo se puede gastar su interés:

```
Premio nuevo = 500.000 · 0,10 = USD 50.000 por año
```

Los premios suman USD 6,05 M/año y el nuevo equilibrio es 6,05 M / 0,10 = USD 60,5 M, así que el fondo queda estable.

### 3.3 Lavabo con goteo (negativa + entrada constante)

Un lavabo recibe 30 cm³/s de una canilla y drena el 10 % de su volumen por segundo.

- **Equilibrio:** `30 = Volumen · 0,1` → **300 cm³** (sin goteo sería 0).
- **Inicio en 500 cm³:** está por encima del equilibrio, así que converge desde arriba. Los 300 cm³ están en equilibrio y los **200 cm³ restantes** drenan con vida media de 7 s: 200 → 100 → 50 → 25…
- **Volumen total:** 500 → 400 → 350 → 325 → … → 300 cm³ cada 7 segundos.

### 3.4 Memorización de letras de canciones (negativa + entrada constante)

Victor escucha un aria que emite 0,5 palabras/s y olvida palabras a razón de `Palabras recordadas / Tiempo de olvido`.

| Parte | Resultado |
|---|---|
| **B.** Tiempo de olvido (recuerda 45 palabras en equilibrio) | `45 / 0,5 =` **90 s** |
| **C.** Palabras tras un aria de 10 min | ≈ **45** (ya está en equilibrio) |
| **D.** Canción de 2 palabras/s (Bob Dylan) | Sube el equilibrio: `2 · 90 =` **180 palabras** |
| **E.** Si tarda más en olvidar (τ mayor) | Recuerda **más**: `S* = c · τ` |

*Aclaración sobre E:* con un τ mayor, la **fracción** de lo recordado que se olvida por segundo es menor, y por eso el nivel de equilibrio del stock es más alto.

---

## 4. Integración gráfica de flujos combinados

El documento D-4596 resuelve un problema relacionado: **dados los flujos de entrada y salida de un stock, ¿cuál es su comportamiento?** Se resuelve con **integración gráfica**.

**Idea central.** El cambio del stock en un intervalo es el área entre la curva de entrada y la de salida:

```
Flujo neto = Entrada − Salida
Stock(t₂) = Stock(t₁) + área bajo el flujo neto entre t₁ y t₂
```

**Reglas prácticas** (del documento):

1. Flujo neto positivo: el stock sube. Negativo: baja.
2. El valor del flujo neto es la **pendiente** del stock en ese instante.
3. Flujo neto constante: el stock cambia **linealmente**.
4. Flujo neto que crece o decrece linealmente (rampa): el stock cambia en forma **parabólica**.
5. Restar dos rectas da otra recta, así que el flujo neto de dos rampas también es una recta.
6. Los gráficos complicados se descomponen en rectángulos y triángulos.

**Ejemplos del documento (tanque de petróleo, verificados en la simulación):**

| Caso | Flujos | Stock en 0 / 5 / 10 / 15 / 20 min |
|---|---|---|
| 3.2 | Entrada 75, salida 50 (constantes), inicio 25 gal | 25 / 150 / 275 / 400 / 525 |
| 3.3 | Entrada `20 + t`, salida 10, inicio 0 | 0 / 62,5 / 150 / 262,5 / 400 |
| 3.4 | Entrada 20 hasta el min 10 y luego `20 + (t − 10)`; salida `40 − 2t`; inicio 100 | 100 / 25 / 0 / 37,5 / 150 |
| 5.4 | Entrada `40 − t`, salida `40 − 2t`, inicio 0 | 0 / 12,5 / 50 / 112,5 / 200 |

**Relación con la simulación mental.** La integración gráfica trabaja con flujos que dependen del tiempo (exógenos); la simulación mental de las secciones 2 y 3 trabaja con flujos que dependen del propio stock (retroalimentación). En ambas, el stock acumula el área de su flujo neto.

![Integración gráfica de flujos combinados](../simulacion/figuras/05_flujos_combinados.png)

---

## 5. Simulación en Vensim: cómo hacerla

### 5.1 ¿Qué es Vensim y para qué se usa acá?

**Vensim** (de Ventana Systems) es un software de dinámica de sistemas. Se dibuja el diagrama de stocks y flujos, se escriben las ecuaciones de cada variable y el programa integra el modelo en el tiempo y grafica los resultados. Acá se usa para **validar la simulación mental**: se calcula a mano, se simula, y los resultados deben coincidir.

La versión gratuita es **Vensim PLE**, libre para uso educativo y personal. Se descarga desde [vensim.com/free-download](https://vensim.com/free-download/) (el sitio puede pedir un correo válido para enviar instrucciones). El documento del MIT incluye los modelos de Vensim equivalentes a cada figura (Figuras 9 a 16), que sirven de referencia.

### 5.2 Paso a paso: modelo de las moscas de la fruta

1. **Crear el modelo.** `File → New Model`. En `Model → Settings` cargar: `INITIAL TIME = 0`, `FINAL TIME = 4`, `TIME STEP = 0.0625`, unidad de tiempo `Day`.
2. **Dibujar el stock.** Herramienta *Box Variable* y clic en el lienzo. Nombrarlo `Fruit Fly Population`.
3. **Dibujar los flujos.** Herramienta *Rate*: clic en el espacio vacío a la izquierda del stock y luego en el stock, para crear el flujo de entrada (`reproduction rate`). Repetir hacia la derecha para el de salida (`removal rate`). Las nubes son fuentes y sumideros fuera del modelo.
4. **Agregar constantes.** Herramienta *Variable*: `REPRODUCTION RATIO` e `INITIAL FRUIT FLY POPULATION`.
5. **Conectar con flechas** (herramienta *Arrow*):
   - `Fruit Fly Population` → `reproduction rate` (cierra el **bucle positivo**);
   - `REPRODUCTION RATIO` → `reproduction rate`;
   - `INITIAL FRUIT FLY POPULATION` → `Fruit Fly Population`.
6. **Escribir las ecuaciones.** Con la herramienta *Equations*, clic en cada variable y completar el editor (ver 5.3). Usar **punto decimal** (`0.5`), no coma.
7. **Verificar.** `Model → Check Model` y `Model → Units Check`.
8. **Simular.** Escribir un nombre de corrida (por ejemplo `eq100`) y presionar *Simulate*. Seleccionar el stock y abrir su gráfico en el panel de análisis.
9. **Comparar corridas.** Cambiar `INITIAL FRUIT FLY POPULATION` a 120, renombrar la corrida (`m120`) y simular de nuevo. Ambas curvas se pueden ver juntas en el gráfico.

> Los nombres de menús y botones pueden variar entre versiones de Vensim. Si algo no aparece donde se indica, buscarlo en `Help` o en la biblioteca de videos de vensim.com.

### 5.3 Ecuaciones de los cuatro modelos

**Modelo 1 · Moscas de la fruta** (`FINAL TIME = 4`, unidad `day`)

```
Fruit Fly Population = INTEG(reproduction rate - removal rate, INITIAL FRUIT FLY POPULATION)
    Units: fruit flies
INITIAL FRUIT FLY POPULATION = 100          (probar con 100, 120 y 80)
    Units: fruit flies
reproduction rate = Fruit Fly Population * REPRODUCTION RATIO
    Units: fruit flies/day
REPRODUCTION RATIO = 0.5
    Units: 1/day
removal rate = 50
    Units: fruit flies/day
```

**Modelo 2 · Fondo del Premio Nobel** (`FINAL TIME = 12`, unidad `year`)

```
Nobel Prize Fund = INTEG(interest - prizes, INITIAL NOBEL PRIZE FUND)
    Units: dollars
INITIAL NOBEL PRIZE FUND = 60000000         (probar con 60e6, 30e6 y 60.5e6)
    Units: dollars
interest = Nobel Prize Fund * INTEREST RATE
    Units: dollars/year
INTEREST RATE = 0.1
    Units: 1/year
prizes = 6000000                            (con el premio nuevo: 6050000)
    Units: dollars/year
```

Para la **parte A** (seis salidas) se agregan seis flujos de salida. Como el documento solo da el total, se puede suponer 1.000.000 por premio (supuesto simplificador del modelo).

**Modelo 3 · Lavabo con goteo** (`FINAL TIME = 40`, unidad `s`)

```
Water in Sink = INTEG(stream in - draining, INITIAL WATER IN SINK)
    Units: cm^3
INITIAL WATER IN SINK = 500                 (probar con 500, 300 y 100)
    Units: cm^3
stream in = 30
    Units: cm^3/s
draining = Water in Sink * DRAINING FRACTION
    Units: cm^3/s
DRAINING FRACTION = 0.1
    Units: 1/s
```

**Modelo 4 · Memorización de letras** (`FINAL TIME = 100` o `600`, unidad `s`)

```
Words Remembered = INTEG(words played - words forgotten, INITIAL WORDS REMEMBERED)
    Units: words
INITIAL WORDS REMEMBERED = 0
    Units: words
words played = 0.5                          (probar con 2 para la canción de Dylan)
    Units: words/s
words forgotten = Words Remembered / TIME TO FORGET
    Units: words/s
TIME TO FORGET = 90
    Units: s
```

### 5.4 Experimentos propuestos

| Experimento | Qué cambiar | Qué debería verse |
|---|---|---|
| Equilibrio | Moscas: inicio = 100 | Línea horizontal en 100 |
| Inestabilidad | Moscas: inicio = 120 y = 80 | 120 crece exponencialmente; 80 cae hasta agotarse |
| Efecto del flujo constante | Moscas con `removal rate = 0` | Crece desde 120 y el equilibrio vuelve a 0 |
| Saldo mínimo | Nobel: inicio = 60 M | Fondo constante |
| Agotamiento | Nobel: inicio = 30 M | Llega a 0 en ≈ 7 años y luego queda negativo |
| Premio nuevo | Nobel: inicio = 60,5 M, `prizes = 6050000` | Fondo constante en 60,5 M |
| Convergencia | Lavabo: inicios 500, 300, 100 | Todos tienden a 300 cm³ |
| Efecto de la entrada | Lavabo con `stream in = 0` | El equilibrio vuelve a 0 |
| Efecto de τ | Letras con Dylan: `TIME TO FORGET` = 90 y = 150 | El equilibrio sube de 180 a 300 palabras |

**Sugerencia:** Vensim tiene *SyntheSim*, que permite mover constantes con deslizadores y ver el gráfico cambiar en tiempo real. Sirve para mostrar en una presentación cómo se desplaza el equilibrio.

### 5.5 Cómo validar con la simulación mental

Para cada corrida, antes de mirar el gráfico:

1. Calcular el equilibrio con `Σ entradas = Σ salidas`.
2. Decidir el modo (equilibrio, se aleja o converge).
3. Estimar el valor en uno o dos tiempos con el tiempo de duplicación o la vida media.
4. Comparar con Vensim. Si no coincide, hay un error de ecuación, de unidades o de signos (en el modelo o en el cálculo mental).

### 5.6 Errores frecuentes

- **Falta la flecha de retroalimentación** del stock hacia el flujo: sin ella no hay bucle.
- **Unidades inconsistentes** (tasa en 1/día con tiempo en años). `Units Check` las detecta.
- **Coma decimal** en las ecuaciones.
- **Paso de tiempo demasiado grande.** Conviene que sea mucho menor que el tiempo característico; si al reducirlo a la mitad los resultados no cambian, está bien.
- **Olvidar el valor inicial** del stock (`INTEG` lo necesita).
- **Interpretar el saldo negativo** del Nobel como real sin revisar los supuestos.

---

## 6. Resultados de la simulación

El script [`simulacion/simulacion.py`](../simulacion/simulacion.py) replica los modelos con la misma integración que Vensim (Euler, `TIME STEP = 0,0625`). La tabla compara el valor simulado con la solución analítica.

| Modelo | Punto | Simulado | Analítico | Teoría |
|---|---|---|---|---|
| Moscas (inicio 120) | Día 4 | 243,3 | 247,8 | 100 + 20·e^(0,5·4) |
| Nobel (inicio 30 M) | Año 12 | −39,2 M | −39,6 M | 60 − 30·e^(0,1·12) |
| Nobel (inicio 30 M) | Fondo = 0 | 7,00 años | 6,93 años | ln 2 / 0,10 |
| Nobel (60,5 M, premio nuevo) | Año 12 | 60,500 M | 60,5 M | Equilibrio |
| Lavabo (inicio 500) | 7 s | 399,1 | 399,3 | 300 + 200·e^(−0,1·7) |
| Lavabo (inicio 500) | 40 s | 303,6 | 303,7 | → 300 |
| Letras (aria) | 100 s | 30,2 | 30,2 | 45·(1 − e^(−100/90)) |
| Letras (aria) | 10 min | 44,9 | 45 | → 45 |
| Letras (Dylan) | 10 min | 179,8 | 180 | → 180 |

Las pequeñas diferencias se deben a que Euler con paso 0,0625 es una aproximación; son mayores en el crecimiento exponencial y desaparecen al reducir el paso.

![Moscas de la fruta](../simulacion/figuras/01_moscas_de_la_fruta.png)

Con 100 moscas la población se mantiene; con 120 crece exponencialmente; con 80 cae hasta extinguirse. El equilibrio es **inestable**.

![Fondo del Premio Nobel](../simulacion/figuras/02_fondo_nobel.png)

El fondo de USD 30 M se agota en alrededor de 7 años. El de USD 60,5 M crece si no se agrega gasto y se estabiliza si se agrega el premio de USD 50.000.

![Lavabo con goteo](../simulacion/figuras/03_lavabo.png)

Sea cual sea el volumen inicial, el sistema converge a 300 cm³. Sin goteo (línea punteada), el equilibrio sería 0.

![Letras de canciones](../simulacion/figuras/04_letras_de_canciones.png)

El equilibrio es la entrada por el tiempo de olvido: 45 palabras para el aria, 180 para la canción rápida y 300 si además se olvida más lento.

---

## 7. Realimentación positiva vs. negativa y aplicación en Ingeniería Industrial

| | Realimentación positiva | Realimentación negativa |
|---|---|---|
| **Qué hace** | Amplifica: el sistema se aleja del equilibrio | Equilibra: converge hacia una meta |
| **Ventajas** | Crecimiento acelerado (interés compuesto); las pequeñas ventajas se multiplican; su equilibrio marca un umbral de viabilidad | Se autocorrige; robusta ante perturbaciones; base de los sistemas de control |
| **Desventajas** | Inestable: todo desvío se amplifica; puede llevar al colapso; requiere control externo | Limita el crecimiento; ajuste gradual según la vida media; su meta depende de los flujos externos |

**Aplicaciones**

- **Inventarios y producción.** Con producción constante `P` y despachos proporcionales al inventario (`I / τ`), el inventario converge a `P · τ`. Con 100 unidades/día y 5 días de permanencia media, se estabiliza en 500 unidades. Es la misma estructura que el lavabo.
- **Fondos y reservas.** El capital mínimo que sostiene un gasto fijo es `gasto / tasa`, igual que en el Fondo Nobel. Sirve, por ejemplo, para dimensionar un fondo de mantenimiento o reposición de equipos.
- **Decisiones rápidas.** Equilibrio, modo y boceto anticipan el comportamiento y los umbrales críticos sin software.
- **Validación de modelos.** La simulación mental permite detectar errores en un modelo de Vensim o Stella antes de confiar en sus resultados.

---

## 8. Conclusiones

1. Un **flujo constante no cambia el tipo de comportamiento** de un sistema de primer orden ni su constante de tiempo: solo **desplaza el equilibrio**.
2. El equilibrio se calcula igualando entradas y salidas: `c / k` en la realimentación positiva y `c · τ` en la negativa.
3. En la **positiva** el equilibrio es un **umbral** (por encima crece, por debajo se agota); en la **negativa** es una **meta** a la que el sistema converge.
4. La **superposición** (equilibrio + exponencial del desvío) permite bocetar el comportamiento completo sin resolver ecuaciones.
5. La simulación mental y la simulación por computadora **se complementan**: la primera da comprensión y permite revisar resultados; la segunda explora escenarios y modelos más complejos.
6. Entender la estructura del sistema permite **diseñar políticas** en lugar de reaccionar a los resultados.

---

## 9. Bibliografía

- Coronado, A. E. (1996). *Beginner Modeling Exercises, Section 4: Mental Simulation: Adding Constant Flows* (D-4546-2). MIT System Dynamics in Education Project. Ejemplos de Vensim agregados por A. Diamond (2001).
- Agatstein, K. y Breierova, L. (1996). *Graphical Integration Exercises, Part Three: Combined Flows* (D-4596). MIT System Dynamics in Education Project.
- Forrester, J. W. (1961). *Industrial Dynamics*. Productivity Press.
- Forrester, J. W. (1968). *Principles of Systems*. Productivity Press.
- Goodman, M. R. (1974). *Study Notes in System Dynamics*. Productivity Press.
- Roberts, N. et al. (1983). *Introduction to Computer Simulation*. Productivity Press.
- Ventana Systems. *Vensim PLE*. https://vensim.com/free-download/

---

## Anexo: reproducir los gráficos

```bash
cd simulacion
pip install -r requirements.txt
python simulacion.py
```
