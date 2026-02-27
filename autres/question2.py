from typing import List, TypeVar

T = TypeVar("T", int, float)

def positifs_croissants(x: List[T]) -> List[T]:
    """
    Retourne les éléments positifs (>= 0) de x triés par ordre croissant.

    Args:
        x (List[T]): liste de nombres (int ou float)

    Returns:
        List[T]: nouvelle liste contenant les éléments positifs de x, triés
    """
    # Filtrer les valeurs positives (a >= 0)
    positifs = [a for a in x if a >= 0]

    # Retourner la liste triée
    return sorted(positifs)

print(positifs_croissants([-5, 2, 0, -1, 3]))

def positifs_croissants2(x: List[T]) -> List[T]:
    """
    Retourne les éléments positifs (>= 0) de x triés par ordre croissant.

    Args:
        x (List[T]): liste de nombres (int ou float)

    Returns:
        List[T]: nouvelle liste contenant les éléments positifs de x, triés
    """
    # Filtrer les valeurs positives (a >= 0)
    positifs = []
    for a in x:
        if a >= 0:
            positifs.append(a)

    # Retourner la liste triée
    return sorted(positifs)

print(positifs_croissants2([-5, 2, 0, -1, 3]))