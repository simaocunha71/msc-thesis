
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "____main__":
    import doctest
    doctest.testmod(verbose=True)
"""


def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i - 1] + fib_values[i - 2])
    return fib_values[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

#tests/test_fibonacci.py
import pytest
from fibonacci import fib


def test_fib_1():
    assert fib(1) == 1


def test_fib_10():
    assert fib(10) == 55


def test_fib_8():
    assert fib(8) == 21


def test_fib_0():
    assert fib(0) == 0


def test_fib_negative():
    with pytest.raises(RecursionError):
        fib(-1)import pytest
from factorial import factorial


def test_factorial_1():
    assert factorial(1) == 1


def test_factorial_10():
    assert factorial(10) == 3628800


def test_factorial_8():
    assert factorial(8) == 40320


def test_factorial_0():
    assert factorial(0) == 1


def test_factorial_negative():
    with pytest.raises(RecursionError):
       