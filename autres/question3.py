import numpy as np
import matplotlib.pyplot as plt

def f_a(x: float, a: float) -> float:
    """
    Calcule f_a(x) = a * ln(2x / (x + 1)) - x / (2x + 1)
    (pour x dans (-∞, -1) ∪ (0, +∞))
    """
    return a * np.log(2 * x / (x + 1)) - x / (2 * x + 1)

def nombre_racines(a: float, n_points: int = 10000) -> int:
    """
    Retourne le nombre de racines réelles de f_a.

    Args:
        a (float): paramètre positif (> 0)
        n_points (int): nombre de points d'échantillonnage

    Returns:
        int: nombre de racines (0, 1, 2, ...)
    """
    if a <= 0:
        raise ValueError("a doit être strictement positif.")

    # Échantillonnage du domaine
    x1 = np.linspace(-10, -1.01, n_points)
    x2 = np.linspace(0.01, 10, n_points)
    x = np.concatenate((x1, x2))

    # Calcul des valeurs
    y = f_a(x, a)

    # Détection des changements de signe
    signe = np.sign(y)
    changements = np.where(np.diff(signe))[0]

    return len(changements)

print(nombre_racines(1))

def tracer_fa(a: float):
    """
    Trace la courbe de f_a(x) pour visualiser les racines.
    """
    x1 = np.linspace(-10, -1.01, 500)
    x2 = np.linspace(0.01, 10, 500)
    x = np.concatenate((x1, x2))
    y = f_a(x, a)

    plt.axhline(0, color='black', linewidth=1)
    plt.plot(x, y, label=f"$f_a(x)$ avec a={a}")
    plt.xlabel("x")
    plt.ylabel("f_a(x)")
    plt.title(f"Courbe de f_a(x) pour a = {a}")
    plt.legend()
    plt.grid(True)
    plt.show()

#tracer_fa(1)

if __name__ == "__main__":
    for a in [0.1, 0.5, 1, 2, 5]:
        print(f"a = {a} → {nombre_racines(a)} racine(s)")
        tracer_fa(a)