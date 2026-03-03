import matplotlib.pyplot as plt
import numpy as np

def fa(a : float, x : float) -> float:
    """
        Function to have the image of the function fa

        Entry: a is a real and x is real
        Exit: the function return fa(x)
        Effect : /
    """
    return a * np.log(2 * x / (x + 1)) - x / (2 * x + 1)

x1 = np.linspace(-5, -1 - 1e-40, 500) #focus de -5 à -1 -1e-40
x2 = np.linspace(1e-40, 5, 500) #focus de 1e-40 à 5
x = np.linspace(-20, 20, 500) #500 points entre -20 et 20

# Create the plot
fig, ax = plt.subplots()  # considérer fig comme figure et ax pour axe.
ax.plot(x, fa(0.1,x), label=r"$f_{0.1}$", color='b', linestyle='-', linewidth=2)
ax.plot(x, fa(1, x), label=r"$f_{1}$", color='m', linestyle='-', linewidth=2)
ax.plot(x, fa(2, x), label=r"$f_{2}$", color='c', linestyle='-', linewidth=2)
ax.plot(x, fa(3, x), label=r"$f_{3}$", color='k', linestyle='-', linewidth=2)
ax.plot(x, fa(5, x), label=r"$f_{5}$", color='orange', linestyle='-', linewidth=2)
ax.plot(x, fa(1000, x), label=r"$f_{1000}$", color='red', linestyle='-', linewidth=2)
# on a en arguments : x, f(x) , légende, couleur, style de ligne et taille de ligne.
# styles de lignes acceptés : solid, dotted, dashed, dashdot
# les styles correspondants : - , : , - , -.

# Add titles and legends
ax.set_ylim(-50, 50)  # limite de hauteur du graphe
ax.legend()

# Center the axes
ax.spines[['left', 'bottom']].set_position('zero')

# Hide the top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#adds grid and shows plot
ax.grid()  # fait la grille (True de base), si on veut False, ne pas mettre la ligne
plt.show()  # affiche le graphique, si non, (block = False)

def nombre_racines(a: float) -> str:
    """
        Function to calculate the number of roots of the function fa

        Entry: a is a real
        Exit: the function return the number of roots of fa
        Effect : /
   """
    if a == 0 or a < 0:
        raise ValueError("a doit être un nombre strictement positif !")
    elif a == (1 / (2 * (np.log(2)))):
        return f"Pour a = {a} on a que fa a 0 racine"
    else:
        return f"Pour a = {a} on a que fa a 1 racine"

#print(nombre_racines(1))