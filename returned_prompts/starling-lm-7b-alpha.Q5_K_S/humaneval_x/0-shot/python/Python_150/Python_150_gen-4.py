    from sympy import isprime
    if isprime(n):
        return x
    else:
        return y






def is_prime(n):
    """
    A simple program which should return True if the number is prime and False otherwise.
    """

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(7)) # True
print(is_prime(15)) # False


def prime_factors(n):
    """
    A simple program which should return the set of prime factors of a number n.

    Examples:
    for prime_factors(12) == {2, 3}
    for prime_factors(100) == {2, 5}
    """

    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

# Test
print(prime_factors(12)) # {2, 3}
print(prime_factors(100)) # {2, 5}


def all_factors(n):
    """
    A simple program which should return the set of all the factors of a number n.
    """

    factors = set()
    for i in range(1, n + 1):
        if n % i == 0:
            factors.add(i)
    return factors

# Test
print(all_factors(12)) # {1, 2, 3, 4, 6, 12}


def sum_of_divisors(n):
    """
    A simple program which should return the sum of all the divisors of