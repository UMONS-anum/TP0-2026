from typing import TypeVar

T = TypeVar('T', float, int, list)

def plus_petit(x : list[T],k : int)-> list[T] :
    """
    Returns the k smallest elements of a list.

    :param x: list of comparable elements by default order
    :param k: Number of elements to return, positive integer
    :return: Returns a list of the k smallest elements
    """
    if k < 0: #nbr d'él demandé négatif, impossible.
        raise ValueError("k doit être positif")
    if len(x) < k: #liste plus petite que le nbr d'él demandés.
        raise ValueError("Nombre d'éléments demandé plus grands que le nombre dans la liste")
    return sorted(x)[:k] # retourne une nouvelle liste triée, ses k premiers éléments.

# .sort() modifie la liste.
# sorted() retourne une nouvelle liste triée, sans modifier l'originale.

def plus_grand(x : list[T],k : int)-> list[T] :
    """
    Returns the k biggest elements of a list.

    :param x: list of comparable elements by default order
    :param k: Number of elements to return, positive integer
    :return: Returns a list of the k biggest elements
    """
    if k < 0 : #nbr d'él demandé négatif, impossible.
        raise ValueError("k doit être positif")
    if len(x) < k :#liste plus petite que le nbr d'él demandés.
        raise ValueError("Nombre d'éléments demandé plus grands que le nombre dans la liste")
    return sorted(x, reverse= True)[:k]

def positifs_croissants(x: list[T]) -> list[T]:
    #retourne les éléments positifs de x triés par ordre croissant
    """
    Returns the positive elements (values >= 0) from a list in ascending order.

    :param x: List of floats, integers or lists of floats and integers.
    :return: A sorted list of positive values.
    """
    positifs = []
    for elem in x:
        if isinstance(elem, list):  # on regarde si l'élément est une liste
            positifs.extend(positifs_croissants(elem))
            # si c'est le cas, on ajoute les réponses de notre récursion à notre liste de réponses
        elif isinstance(elem, (int, float)) and elem >= 0:  # si l'élément est un nombre positif
            positifs.append(elem)  # on l'ajoute à la réponse
            # donc, si c'est pas une liste ou un nombre, on l'ignore
    return sorted(positifs)
