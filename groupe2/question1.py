def plus_petits[T](x: list[T], k: int) -> list[T]:
    """
        Entrée: x une liste de générique, k un entier positif  
        Sortie: une liste des k plus petits éléments de x
        Effet: /
        Crée une nouvelle liste étant x triée avec la fonction sorted().
        Une exception est levée si k dépasse la longueur de x ou s'il est strictement négatif.
    """
    x_sort: list[T] = sorted(x)
    if k > len(x) or k < 0:
        raise ValueError("k doit être compris entre 0 et la longueur de la liste")
    elif k == 0:
        return []
    else:
        return x_sort[:k]    
    
    
def plus_grands[T](x: list[T], k: int) -> list[T]:
    """
        Entrée: x une liste de générique, k un entier positif  
        Sortie: une liste des k plus grands éléments de x
        Effet: /
        Crée une nouvelle liste étant x triée avec la fonction sorted().
        Une exception est levée si k dépasse la longueur de x ou s'il est strictement négatif.
    """
    x_sort: list[T] = sorted(x)
    if k > len(x) or k < 0:
        raise ValueError("k doit être compris entre 0 et la longueur de la liste")
    elif k == 0:
        return []
    else:
        return x_sort[-k:]