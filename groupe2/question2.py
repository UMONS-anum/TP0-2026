def positifs_croissants(x: list[float]) -> list[float]:
    """
       Entrée: x une liste de float
       Sortie: une liste des éléments postifs de x
       Effet: /
       Crée une nouvelle liste étant x triée avec la fonction sorted().
       Tant que i est inférieur à la longueur de la liste 
       et l'élément en position i est strictement négatif
       alors on incrémente i de 1.
    """
    x_sort: list[float] = sorted(x)
    i: int = 0
    while i < len(x_sort) and x_sort[i] < 0:
        i+=1
    if i == len(x):
        return []    
    else:
        return x_sort[i:]