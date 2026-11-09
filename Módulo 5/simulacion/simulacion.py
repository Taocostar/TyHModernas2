"""
Simulación de los modelos de stocks y flujos del TP 5
Técnicas y Herramientas Modernas 2 - Ingeniería Industrial

Replica en Python los modelos que se construyen en Vensim:
  1. Población de moscas de la fruta (realimentación positiva + salida constante)
  2. Fondo del Premio Nobel         (realimentación positiva + salida constante)
  3. Lavabo con goteo               (realimentación negativa + entrada constante)
  4. Memorización de letras         (realimentación negativa + entrada constante)
  5. Integración gráfica de flujos combinados (tanque de petróleo / agua)

Igual que Vensim, el stock se calcula con el método de Euler:
    stock(t + dt) = stock(t) + (entradas - salidas) * dt
con TIME STEP = 0,0625.

Uso:
    pip install -r requirements.txt
    python simulacion.py
Los gráficos se guardan en la carpeta ./figuras
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DT = 0.0625  # TIME STEP de los modelos Vensim del documento
SALIDA = Path(__file__).parent / "figuras"
SALIDA.mkdir(exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 130,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.size": 10,
})


def simular(stock0, flujo_neto, t_final, dt=DT):
    """Integra un stock con Euler. flujo_neto(t, stock) devuelve entradas - salidas."""
    n = int(round(t_final / dt))
    t = np.linspace(0, n * dt, n + 1)
    s = np.empty(n + 1)
    s[0] = stock0
    for i in range(n):
        s[i + 1] = s[i] + flujo_neto(t[i], s[i]) * dt
    return t, s


# --------------------------------------------------------------------------
# 1. Moscas de la fruta: realimentación positiva con salida constante
# --------------------------------------------------------------------------
def moscas():
    razon, remocion = 0.5, 50.0           # 1/día ; moscas/día
    equilibrio = remocion / razon         # = 100 moscas
    neto = lambda t, s: s * razon - remocion

    t, m100 = simular(100, neto, 4)
    _, m120 = simular(120, neto, 4)
    _, m80 = simular(80, neto, 4)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, m120, label="Inicio 120 moscas (crece)", color="#c0392b", lw=2)
    ax.plot(t, m100, label="Inicio 100 moscas (equilibrio)", color="#2c3e50", lw=2)
    ax.plot(t, np.maximum(m80, 0),
            label="Inicio 80 moscas (se extingue; no hay moscas negativas)",
            color="#2980b9", lw=2)
    ax.axhline(equilibrio, color="gray", ls="--", lw=1)
    ax.text(0.05, equilibrio + 6, f"Equilibrio = {remocion:.0f} / 0,5 = {equilibrio:.0f}",
            color="gray", fontsize=9)
    ax.set_xlabel("Días")
    ax.set_ylabel("Moscas de la fruta")
    ax.set_title("Moscas de la fruta: equilibrio inestable (positiva + salida constante)")
    ax.set_ylim(0, 280)
    ax.legend(loc="upper left", fontsize=8)
    fig.tight_layout()
    fig.savefig(SALIDA / "01_moscas_de_la_fruta.png")
    plt.close(fig)

    print("\n[1] MOSCAS DE LA FRUTA")
    print(f"  Equilibrio teórico: {equilibrio:.0f}")
    print(f"  Tiempo de duplicación aprox. 0,7/0,5 = {0.7 / razon:.2f} días "
          f"(exacto ln2/0,5 = {np.log(2) / razon:.3f})")
    for dia in (0, 1.4, 2.8, 4):
        i = int(round(dia / DT))
        analitico = equilibrio + 20 * np.exp(razon * t[i])
        print(f"  Día {t[i]:.2f}: simulado = {m120[i]:6.1f} | analítico = {analitico:6.1f}")


# --------------------------------------------------------------------------
# 2. Fondo del Premio Nobel
# --------------------------------------------------------------------------
def nobel():
    tasa, premios = 0.10, 6.0             # 1/año ; millones $/año
    equilibrio = premios / tasa           # = 60 M
    neto = lambda t, s: s * tasa - premios

    t, f30 = simular(30, neto, 12)
    _, f60 = simular(60, neto, 12)
    _, f605 = simular(60.5, neto, 12)
    # Parte E: con el nuevo premio (50 mil) el fondo de 60,5 M queda estable
    _, f605_nuevo = simular(60.5, lambda t, s: s * tasa - (premios + 0.05), 12)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

    # Panel izquierdo: fondo en el equilibrio y por debajo
    ax1.plot(t, f60, label=r"Inicio \$60 M (equilibrio)", color="#2c3e50", lw=2)
    ax1.plot(t, f30, label=r"Inicio \$30 M (se agota en ~7 años)", color="#c0392b", lw=2)
    ax1.axhline(0, color="black", lw=0.8)
    ax1.axhline(equilibrio, color="gray", ls="--", lw=1)
    ax1.set_xlabel("Años")
    ax1.set_ylabel(r"Millones de \$")
    ax1.set_title(r"Partes C y D: equilibrio y fondo de \$30 M", fontsize=9)
    ax1.legend(fontsize=8, loc="lower left")

    # Panel derecho: zoom sobre el fondo de 60,5 M (parte E)
    ax2.plot(t, f605, label=r"\$60,5 M sin premio nuevo (crece)", color="#27ae60", lw=2)
    ax2.plot(t, f605_nuevo, label=r"\$60,5 M con premio nuevo de \$50 mil (estable)",
             color="#8e44ad", lw=2, ls="--")
    ax2.axhline(equilibrio, color="gray", ls="--", lw=1)
    ax2.text(0.2, equilibrio + 0.08, r"Equilibrio original: \$60 M", color="gray", fontsize=8)
    ax2.set_xlabel("Años")
    ax2.set_ylabel(r"Millones de \$")
    ax2.set_ylim(59.8, 62.0)
    ax2.set_title(r"Parte E: el excedente de \$0,5 M paga el premio nuevo", fontsize=9)
    ax2.legend(fontsize=8, loc="upper left")

    fig.suptitle(r"Fondo del Premio Nobel (interés 10 % anual, premios \$6 M/año)", fontsize=11)
    fig.tight_layout()
    fig.savefig(SALIDA / "02_fondo_nobel.png")
    plt.close(fig)

    idx = np.argmax(f30 <= 0)  # primer instante con fondo <= 0
    print("\n[2] FONDO NOBEL")
    print(f"  Saldo mínimo (equilibrio): ${equilibrio:.0f} M")
    print(f"  Duplicación del déficit: 0,7/0,10 = {0.7 / tasa:.1f} años "
          f"(exacto ln2/0,10 = {np.log(2) / tasa:.2f})")
    print(f"  Fondo de $30 M llega a $0 en t = {t[idx]:.2f} años "
          f"(analítico: {np.log(2) / tasa:.2f})")
    print(f"  Fondo de $30 M a los 12 años: {f30[-1]:.1f} M (analítico: "
          f"{equilibrio - 30 * np.exp(tasa * 12):.1f})")
    print(f"  Parte E: premio nuevo = $0,5 M x 0,10 = ${0.5 * tasa * 1000:.0f} mil/año")
    print(f"  Fondo $60,5 M con premio nuevo a los 12 años: {f605_nuevo[-1]:.3f} M")


# --------------------------------------------------------------------------
# 3. Lavabo: realimentación negativa con entrada constante
# --------------------------------------------------------------------------
def lavabo():
    entrada, fraccion = 30.0, 0.1         # cm3/s ; 1/s
    equilibrio = entrada / fraccion       # = 300 cm3
    neto = lambda t, s: entrada - s * fraccion

    t, v500 = simular(500, neto, 40)
    _, v300 = simular(300, neto, 40)
    _, v100 = simular(100, neto, 40)
    _, v500_sin = simular(500, lambda t, s: -s * fraccion, 40)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, v500, label="Inicio 500 cm³ (baja hacia 300)", color="#c0392b", lw=2)
    ax.plot(t, v300, label="Inicio 300 cm³ (equilibrio)", color="#2c3e50", lw=2)
    ax.plot(t, v100, label="Inicio 100 cm³ (sube hacia 300)", color="#2980b9", lw=2)
    ax.plot(t, v500_sin, label="Inicio 500 cm³, sin goteo (baja a 0)",
            color="gray", lw=1.5, ls=":")
    ax.axhline(equilibrio, color="gray", ls="--", lw=1)
    ax.set_xlabel("Segundos")
    ax.set_ylabel("Agua en el lavabo (cm³)")
    ax.set_title("Lavabo con goteo: el equilibrio se desplaza de 0 a 300 cm³")
    ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    fig.savefig(SALIDA / "03_lavabo.png")
    plt.close(fig)

    print("\n[3] LAVABO")
    print(f"  Equilibrio: {entrada:.0f} / {fraccion} = {equilibrio:.0f} cm3")
    print(f"  Vida media aprox. 0,7/0,1 = {0.7 / fraccion:.0f} s "
          f"(exacto ln2/0,1 = {np.log(2) / fraccion:.2f})")
    for seg in (0, 7, 14, 21, 40):
        i = int(round(seg / DT))
        analitico = equilibrio + 200 * np.exp(-fraccion * t[i])
        print(f"  t = {t[i]:4.1f} s: simulado = {v500[i]:6.1f} | analítico = {analitico:6.1f}")


# --------------------------------------------------------------------------
# 4. Memorizar letras de canciones
# --------------------------------------------------------------------------
def letras():
    tiempo_olvido = 90.0                  # s
    aria, dylan = 0.5, 2.0                # palabras/s
    neto = lambda entrada: (lambda t, s: entrada - s / tiempo_olvido)

    t, w_aria = simular(0, neto(aria), 600)
    _, w_dylan = simular(0, neto(dylan), 600)
    _, w_dylan_lento = simular(0, lambda t, s: dylan - s / 150.0, 600)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, w_dylan_lento, label="Dylan, olvida más lento (τ = 150 s) → 300",
            color="#27ae60", lw=2)
    ax.plot(t, w_dylan, label="Dylan, 2 palabras/s → 180", color="#c0392b", lw=2)
    ax.plot(t, w_aria, label="Aria, 0,5 palabras/s → 45", color="#2c3e50", lw=2)
    ax.axvline(180, color="gray", ls=":", lw=1)
    ax.text(185, 8, "3 min", color="gray", fontsize=8)
    ax.set_xlabel("Segundos")
    ax.set_ylabel("Palabras recordadas")
    ax.set_title("Memorizar letras: el equilibrio es entrada × tiempo de olvido")
    ax.set_ylim(0, 400)
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(SALIDA / "04_letras_de_canciones.png")
    plt.close(fig)

    print("\n[4] LETRAS DE CANCIONES")
    print(f"  Tiempo de olvido = 45 / 0,5 = {45 / aria:.0f} s")
    print(f"  Aria a los 10 min: {w_aria[-1]:.1f} palabras (equilibrio {aria * tiempo_olvido:.0f})")
    print(f"  Dylan a los 10 min: {w_dylan[-1]:.1f} palabras (equilibrio {dylan * tiempo_olvido:.0f})")
    print(f"  Aria a los 100 s (FINAL TIME del modelo Vensim): "
          f"{w_aria[int(round(100 / DT))]:.1f} palabras")


# --------------------------------------------------------------------------
# 5. Integración gráfica de flujos combinados (documento D-4596)
# --------------------------------------------------------------------------
def flujos_combinados():
    casos = {
        "3.2  Entrada 75, salida 50 (constantes), inicio 25 gal":
            (25, lambda t: 75.0, lambda t: 50.0),
        "3.3  Entrada 20 + t, salida 10, inicio 0":
            (0, lambda t: 20.0 + t, lambda t: 10.0),
        "3.4  Entrada 20 → 20 + (t−10), salida 40 − 2t, inicio 100":
            (100, lambda t: 20.0 if t < 10 else 20.0 + (t - 10), lambda t: 40.0 - 2.0 * t),
        "5.4  Entrada 40 − t, salida 40 − 2t, inicio 0":
            (0, lambda t: 40.0 - t, lambda t: 40.0 - 2.0 * t),
    }

    fig, axes = plt.subplots(2, 2, figsize=(10, 6.5))
    print("\n[5] FLUJOS COMBINADOS (stock en min 0, 5, 10, 15, 20)")
    for ax, (titulo, (s0, entrada, salida)) in zip(axes.ravel(), casos.items()):
        t, s = simular(s0, lambda t, st: entrada(t) - salida(t), 20, dt=0.01)
        ax.plot(t, s, color="#2c3e50", lw=2)
        ax.set_title(titulo, fontsize=8)
        ax.set_xlabel("Minutos")
        ax.set_ylabel("Galones")
        valores = [s[int(round(m / 0.01))] for m in (0, 5, 10, 15, 20)]
        print("  " + titulo.split("  ")[0] + ": " + ", ".join(f"{v:.1f}" for v in valores))
    fig.suptitle("Integración gráfica: stock = stock inicial + área entre entrada y salida",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(SALIDA / "05_flujos_combinados.png")
    plt.close(fig)


if __name__ == "__main__":
    moscas()
    nobel()
    lavabo()
    letras()
    flujos_combinados()
    print(f"\nGráficos guardados en: {SALIDA}")
