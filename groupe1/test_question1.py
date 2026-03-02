import pytest

from question1 import plus_petits, plus_grands, positifs_croissants


def test_plus_petits():
    assert plus_petits([3, 1, 2], 2) == [1, 2]


def test_plus_grands():
    assert plus_grands([3, 1, 2], 2) == [3, 2]


def test_k_zero_ou_negatif():
    assert plus_petits([1, 2, 3], 0) == []
    assert plus_petits([1, 2, 3], -5) == []
    assert plus_grands([1, 2, 3], 0) == []
    assert plus_grands([1, 2, 3], -1) == []


def test_k_trop_grand():
    assert plus_petits([3, 1, 2], 99) == [1, 2, 3]
    assert plus_grands([3, 1, 2], 99) == [3, 2, 1]


def test_sous_question_1():
    x = [[2], [33, 1], [1, 7]]
    assert plus_petits(x, 2) == [[1, 7], [2]]


def test_sous_question_2():
    x = [[2], [3, 2], [3, 1]]
    y = plus_petits(x, 2)  # [[2], [3, 1]]
    for a in y:
        a.sort()
    # Comme y contient des références vers des sous-listes de x, x est modifié.
    assert x == [[2], [3, 2], [1, 3]]

# test question 2

def test_positifs_croissants():
    assert positifs_croissants([]) == []
    assert positifs_croissants([3, -1, 0, 5, -4, 2]) == [0, 2, 3, 5]
