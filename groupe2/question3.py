from math import log as log

def nombre_racines(a: float)-> int:
    """
        Entrée: a un float
        Sortie: En fonction des valeurs de a strictement positif,
                cela retourne le nombre de racines de la fonction f_a(x) = aln(2x/(x+1))-x/(2x+1).
        Effet: /
        Une erreur est levée si la valeur de a n'est pas strictement positive.        
    """
    if a <= 0:
        raise ValueError("le paramètre doit être un réel stictement positif")
    elif a == 1/(2*log(2)):
        return 0
    else:
        return 1