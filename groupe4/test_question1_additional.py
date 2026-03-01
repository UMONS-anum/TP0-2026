import pytest
from question1 import plus_petits, plus_grands


@pytest.mark.parametrize("data,k,expected", [
    ([3, 1, 2], 2, [1, 2]),
    ([5, 4], 5, [4, 5]),
    ([1, 2, 3], 0, []),
    ([2, 2, 1], 2, [1, 2]),
])
def test_plus_petits_numbers(data, k, expected):
    assert plus_petits(data, k) == expected


@pytest.mark.parametrize("data,k,expected", [
    ([3, 1, 2], 2, [2, 3]),
    ([5, 4], 5, [4, 5]),
    ([1, 2, 3], 0, []),
    ([2, 2, 1], 2, [2, 2]),
])
def test_plus_grands_numbers(data, k, expected):
    assert plus_grands(data, k) == expected