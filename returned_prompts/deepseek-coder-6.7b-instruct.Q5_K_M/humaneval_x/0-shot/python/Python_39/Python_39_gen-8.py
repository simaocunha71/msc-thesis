
    def is_prime(num: int):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    count = 0
    i = 1
    while count < n:
        f = fib(i)
        if is_prime(f):
            count += 1
        i += 1
    return f


if __name__ == "__main__":
    import doctest

    doctest.testmod()

#tests/test_main.py
import pytest
from prime_fib import prime_fib


@pytest.mark.parametrize(
    "n, expected", [(1, 2), (2, 3), (3, 5), (4, 13), (5, 89), (6, 233), (7, 1597)]
)
def test_prime_fib(n, expected):
    assert prime_fib(n) == expected


def test_prime_fib_negative():
    with pytest.raises(ValueError):
        prime_fib(-1)


def test_prime_fib_non_int():
    with pytest.raises(TypeError):
        prime_fib(1.5)


def test_prime_fib_non_numeric():
    with pytest.raises(TypeError):
        prime_fib("abc")


def test_prime_fib_zero():
    assert prime_fib(0) == 0


def test_prime_fib_large():
    assert prime_fib(10) == 44945570212853