

def add(x: int, y: int):
    return x + y
"""


def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

#python_tests/test_sub.py
from main import sub


def test_sub():
    assert sub(3, 2) == 1
    assert sub(7, 5) == 2

#python_tests/test_square.py
from main import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9

#python_tests/test_square_root.py
from main import square_root


def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3

#python_tests/test_sum.py
from main import sum


def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([4, 5, 6]) == 15

#python_tests/test_sum_of_squares.py
from main import sum_of_squares


def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3]) == 14
    assert sum_of_squares([4, 5, 6]) == 162import pytest


def test_add():
    assert 2 + 2 == 5


def test_sub():
    assert 3 - 2 == 1


def test_mult():
    assert 2 * 2 == 4


def test_div():
    assert 4 / 2 == 2


def test_power():
    assert 2 ** 3 == 8


def test_modulo():
    assert 10 % 3 == 1


def test_floordiv():
    assert 10 // 3 == 3


def test_list_append():
    l = [1, 2, 3]
    l.append(4)
    assert l == [1,