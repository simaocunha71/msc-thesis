"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
from math import ceil, sqrt
def is_not_prime(n):
    def get_factors(n):  # O(sqrt (n))
        if n == 1:
            return [1]
        elif n < 4:
            return list(range(2, n + 1))
        else:
            for factor in list(range(2, int(ceil(sqrt(n))) + 1)):
                yield factor if n % factor == 0 and get_factors(factor)[-1] != 1 else 0
    return any(get_factors(n) != [1])
