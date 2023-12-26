from typing import List


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

    prime_factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            j = 1
            while j <= n // i and n % (i * j) == 0:
                j *= i
            prime_factors.append((j, i))
    return list(reversed(set(prime_factors)))