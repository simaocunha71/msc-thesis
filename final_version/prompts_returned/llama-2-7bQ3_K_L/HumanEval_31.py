

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    
    if n < 2:
        return False
    
    divisors = 2 * [True] + list([False for _ in range(*[0]*n)]), 3, 5, 7, 9, 11, 13, 17, 19, 23, 29
    
    return any(
        not divisor for divisor in divisors if n % divisor == 0
    )




