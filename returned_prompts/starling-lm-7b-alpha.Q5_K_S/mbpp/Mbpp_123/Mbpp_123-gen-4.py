"""
def amicable_numbers_sum(limit):
    """
    Returns the sum of all amicable numbers from 1 to limit (inclusive).

    An amicable number is a number that is equal to the sum of its proper divisors (excluding the number itself).
    """
    total = 0
    for n in range(1, limit + 1):
        total += sum_proper_divisors(n)
    return total

def sum_proper_divisors(n):
    """
    Returns the sum of the proper divisors of n.
    """
    if n == 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            total += i + n // i
    return total

def is_amicable(n):
    """
    Returns True if n is an amicable number, and False if not.
    """
    return sum_proper_divisors(n) == n
"""

def amicable_numbers_sum(limit):
    """
    Returns the sum of all amicable numbers from 1 to limit (inclusive).

    An amicable number is a number that is equal to the sum of its proper divisors (excluding the number itself).
    """
    total = 0
    for n in range(1, limit + 1):
        if is_amicable(n):
            total += n
    return total

def sum_proper_divisors(n):
    """
    Returns the sum of the proper divisors of n.
    """
    if n == 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            total += i + n // i
    return total

def is_amicable(n):
    """
    Returns True if n is an amicable number, and False if not.
    """
    return sum_proper_divisors(n)