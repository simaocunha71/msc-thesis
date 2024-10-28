

def greatest_common_divisor(a: int, b: int)  -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#tests/test_gcd.py
import pytest
from gcd import greatest_common_divisor

def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(14, 21) == 7
    assert greatest_common_divisor(100, 10) == 10
    assert greatest_common_divisor(111, 222) == 111
    assert greatest_common_divisor(17, 5) == 1
    assert greatest_common_divisor(1, 1) == 1
    assert greatest_common_divisor(0, 1) == 1
    with pytest.raises(TypeError):
        greatest_common_divisor('1', 1)
    with pytest.raises(TypeError):
        greatest_common_divisor(1, '1')
    with pytest.raises(TypeError):
        greatest_common_divisor('1', '1')
    with pytest.raises(TypeError):
        greatest_common_divisor(None, 1)
    with pytest.raises(TypeError):
        greatest_common_divisor(1, None)
    with pytest.raises(TypeError):
        greatest_common_divisor(None, None)