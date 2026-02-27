from question1 import plus_petits, plus_grands

def test_plus_petits():
    assert plus_petits([5, 1, 3, 2], 2) == [1, 2]
    assert plus_petits(["c", "a", "b"], 2) == ["a", "b"]
    assert plus_petits([[2], [33, 1], [1, 7]], 2) == [[1, 7], [2]]

def test_plus_grands():
    assert plus_grands([5, 1, 3, 2], 2) == [3, 5]
    assert plus_grands(["c", "a", "b"], 2) == ["b", "c"]
    assert plus_grands([[2], [33, 1], [1, 7]], 2) == [[2], [33, 1]]