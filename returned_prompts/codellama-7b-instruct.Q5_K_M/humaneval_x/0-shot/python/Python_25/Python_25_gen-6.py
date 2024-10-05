def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    return factors

# Tests

from random import randint
from math import sqrt


def random_prime(n: int) -> int:
    """ Generate random prime number of given length """

    assert n > 2, "Prime number should have length greater than 2"

    while True:
        rand = randint(2 ** (n - 1), 2 ** n - 1)
        if is_prime(rand):
            return rand


def random_composite(n: int) -> int:
    """ Generate random composite number of given length """

    assert n > 2, "Composite number should have length greater than 2"

    while True:
        rand = randint(2 ** (n - 1), 2 ** n - 1)
        if not is_prime(rand):
            return rand


def is_prime(n: int) -> bool:
    """ Check if given number is prime """

    assert n > 1, "Number should be greater than 1"

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 