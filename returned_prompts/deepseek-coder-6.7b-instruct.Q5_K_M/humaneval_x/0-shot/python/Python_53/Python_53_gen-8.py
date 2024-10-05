

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


# print(add(2, 3))
# print(add(5, 7))

#tests/test_add.py
import pytest
from main import add


def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(10, 20) == 30
    assert add(0, 0) == 0


def test_add_negative():
    assert add(-2, 3) == 1
    assert add(-5, -7) == -12
    assert add(10, -20) == -10
    assert add(0, -5) == -5


def test_add_type_error():
    with pytest.raises(TypeError):
        add("1", "2")
    with pytest.raises(TypeError):
        add(1)
    with pytest.raises(TypeError):
        add(None, 1)
    with pytest.raises(TypeError):
        add([1, 2], [3, 4])