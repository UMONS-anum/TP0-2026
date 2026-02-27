from typing import List, TypeVar

# Type générique pour tout élément comparable
T = TypeVar("T")

def plus_petits(x: List[T], k: int) -> List[T]:
    """
    Retourne les k plus petits éléments de la liste x.

    Args:
        x (List[T]): liste d’éléments comparables
        k (int): nombre d’éléments à extraire

    Returns:
        List[T]: nouvelle liste contenant les k plus petits éléments triés
    """
    return sorted(x)[:k]


def plus_grands(x: List[T], k: int) -> List[T]:
    """
    Retourne les k plus grands éléments de la liste x.

    Args:
        x (List[T]): liste d’éléments comparables
        k (int): nombre d’éléments à extraire

    Returns:
        List[T]: nouvelle liste contenant les k plus grands éléments triés
    """
    return sorted(x)[-k:]

"""print(plus_petits([[2, 42], [33, 1], [1, 7, 4], [2, 4]], 2))
print(plus_grands([[2], [33, 1], [1, 7]], 2))
print(plus_petits(["c", "a", "b"], 2))"""

x = [[2, 1], [33, 1], [7, 1]]
y = plus_petits(x, 2)
for a in y:
    a.sort()
print(x)