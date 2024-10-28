    primes = []

    if n == 0:
        return []

    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes


def is_prime(n: int) -> bool:
    """ Check if a given number is prime.
    >>> is_prime(3)
    True
    >>> is_prime(1)
    False
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """

    if n < 2:
        return False

    for idx in range(2, int(n ** 0.5) + 1):
        if n % idx == 0:
            return False

    return True


