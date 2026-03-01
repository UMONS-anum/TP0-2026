from typing import List, TypeVar

T = TypeVar("T")

def plus_petits(x: List[T],k: int) -> List[T] :
    if k<= 0:           # cas où k est nul ou negative (cas vide)
        return []
    else:               # cas où k est positif
        return sorted(x)[:k]  # retourne les k premiers éléments (donc les k plus petit car la liste est triée)

def plus_grands(x: List[T],k: int) -> List[T]:
    if k<= 0:        # cas où k est nul ou negative (cas vide)
        return []
    else:           #cas où k positif
        return sorted(x)[len(x)-k:]  # #retourne les k derniers éléments de la liste triée