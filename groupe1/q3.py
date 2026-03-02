from matplotlib import pyplot as plt
import numpy as np

def f(a, x):
    """
    Retourne f_a(x)
    """
    return a * np.log((2*x)/(x+1)) - x/(2*x+1)

def nombre_racines(a: float) -> int:
    """
    Retourne le nombre de racines de f_a en fonction du a passé en paramètre

    Args:
        float: a

    Return:
        int: le nombre de racine de f_a
    """
    if a == 1/(2*np.log(2)):
        return 0
    else:
        return 1


if __name__ == "__main__":
    # Affichage de f_a(x) pour différentes valeurs de a

    a_values = [0.1, 0.25, 1/(2*np.log(2)), 1]
    x = np.linspace(-10, 10, 500)
    plt.figure(figsize=(10, 6))

    for a in a_values:
        y = f(a, x)
        plt.plot(x, y, label=f"a = {a:.4f}")

    plt.title("Courbes de f(a, x) pour différentes valeurs de a")
    plt.xlabel("x")
    plt.ylabel("f(a, x)")
    plt.legend()
    plt.grid(True)
    plt.show()

