import math
import numpy as np  # importe une bibliothèque de calcul
import matplotlib.pyplot as plt  # importe le module pour tracer ta fonction
from matplotlib.widgets import Slider, Button  # import les widgets curseurs et boutons


class Enonce (Exception) :
    """
    Exception lancée lorsqu'on ne respecte pas l'énoncé.
    """

    def __init__(self, msg="Veuillez respecter l'énoncé."):
        super().__init__(msg)

    pass

def f (a:float, x:float) -> float :
    """
    Fournit les valeurs de la fonction f_a.

    Args:
        a (float) : le paramètre strictement positif de la fonction
        x (float) : la variable

    Raises:
        Enonce : se déclanche lorsque les données ne correspondent pas à l'énoncé

    Returns:
        (float) : l'image de x par f_a
    """

    if a<=0 :
        raise Enonce("Alpha doit être un réel strictement positif.")

    return a*np.log((2*x)/(x+1)) -(x)/(2*x+1)

def nombre_racines (a:float) -> int :
      if a== 1/(2*math.log(2)):       # voir preuve rapport
        return 0
      if a<=0:                         #alpha doit être positif 
        raise  Enonce("a doit être un réel strictement positif.")
      else:                         #voir preuve rapport 
        return 1


def affiche_f (a:float) -> None :

    x = np.linspace(0.001, 30, 1000)  # crée un tableau de 1.000 valeurs comprises entre 0.001 et 30
    x_bis = np.linspace(-30, -1.001,1000)

    fig, ax = plt.subplots()  # création de la fenêtre et des axes
    plt.subplots_adjust(left=0.25, bottom=0.40)  # met de l'espace en dessous du graphique pour y placer les sliders
    line, = ax.plot(x, f(a, x), lw=2)  # tracer la fonction f avec le paramètre a initial
    line_bis, = ax.plot(x_bis, f(a, x_bis), lw=2)

    ax.set_title("Graph de f_a")  # titre du graphique
    ax.set_xlim(-30,30)  # fixe l'axe Y entre -5 et 5
    ax.set_ylim(-5, 5)  # fixe l'axe Y entre -5 et 5
    ax.set_xlabel("X")  # nom de l'axe des absisces
    ax.set_ylabel("Y")  # nom de l'axe des ordonnées
    ax.minorticks_on()  # active les graduations
    ax.grid(which='major', linestyle='-', linewidth=0.8)  # grille principale
    ax.grid(which='minor', linestyle='--', linewidth=0.5)  # grille secondaire plus fine

    ax_a = plt.axes(
        [0.25, 0.25, 0.65, 0.03])  # crée une zone pour le slider au format : [gauche, bas, largeur, hauteur]
    slider_a = Slider(
        ax_a,  # axe graphique du slider
        'a',  # nom du slider
        0.01,  # valeur minimale
        10,  # valeur maximale
        valinit=1  # valeur initiale
    )

    ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])  # crée une zone pour le bouton "Reset"
    button = Button(ax_button, 'Reset')  # crée le bouton "Reset"

    def update(val):
        """ Fonction appelée automatiquement dès qu’un slider est déplacé."""

        a = slider_a.val  # récupère la valeur actuelle du slider "a"
        y = f(a, x) # recalcule de la fonction avec la nouvelle valeur de alpha
        y_bis = f(a, x_bis)
        line.set_ydata(y)  # met à jour les données Y
        line_bis.set_ydata(y_bis)
        fig.canvas.draw_idle()  # redessine le graphique

    slider_a.on_changed(update)  # quand le slider "a" bouge, on appelle update()

    def reset(event):
        """
        Fonction appelée quand on clique sur le bouton "Reset".
        """
        slider_a.reset()  # remet le slider "a" à la valeur initiale

    button.on_clicked(reset)  # connecte le bouton à la fonction reset

    plt.show()  # lance le programme


if __name__=='__main__' :
    # pour afficher le graphe et pouvoir interagir avec le slider,
    # appelez directement affiche_f(1.0)
    affiche_f(1.0)