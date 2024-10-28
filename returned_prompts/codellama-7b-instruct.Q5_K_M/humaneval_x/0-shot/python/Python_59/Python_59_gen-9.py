
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 1:
        return -1
    for i in range(int(n ** 0.5), 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    return -1

def is_prime(n: int):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
