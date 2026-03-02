"""
Remarques:
- On utilise 'sorted()' qui renvoie une nouvelle liste plutôt que 'list.sort()'
  qui modifie la liste initiale.
- Complexité (tri Python = Timsort) :
  - pire cas : O(n log n)
- Ici, on trie toute la liste puis on prend une tranche : O(n log n).
"""

from __future__ import annotations

from typing import Protocol, TypeVar


class Comparable(Protocol):
    """Un objet comparable avec l'ordre usuel (au minimum __lt__)."""
    def __lt__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def plus_petits(x: list[T], k: int) -> list[T]:
    """
    Renvoie les k plus petits éléments de x, dans l'ordre croissant.
    - Ne modifie pas x.
    - Si k <= 0 : renvoie [].
    - Si k >= len(x) : renvoie tous les éléments triés.
    """
    if k <= 0:
        return []
    return sorted(x)[:k]


def plus_grands(x: list[T], k: int) -> list[T]:
    """
    Renvoie les k plus grands éléments de x, dans l'ordre décroissant.
    - Ne modifie pas x.
    - Si k <= 0 : renvoie [].
    - Si k >= len(x) : renvoie tous les éléments triés décroissants.
    """
    if k <= 0:
        return []
    return sorted(x, reverse=True)[:k]

#Réponses aux questions :
"""
Que doit retourner plus_petit([[2], [33, 1], [1, 7]], 2)?
-> [[1, 7], [2]]

Qu’est-ce que le code suivant imprime (en expliquant pourquoi, en fonction de votre implémentation de plus_petits) ?
x = [[2], [3, 2], [3, 1]]
y = plus_petits(x, 2)
    for a in y:
        a.sort()
print(x)

-> [[2], [3, 2], [1, 3]]
car y = [[2], [3, 1]] et a.sort() modifie les listes dans y qui sont les mêmes que dans x.
"""

#question 2
def positifs_croissants(x: list[float]) -> list[float]:
    """
    Retourne les éléments >= 0 de x triés par ordre croissant.
    """

    return sorted(a for a in x if a >= 0)
