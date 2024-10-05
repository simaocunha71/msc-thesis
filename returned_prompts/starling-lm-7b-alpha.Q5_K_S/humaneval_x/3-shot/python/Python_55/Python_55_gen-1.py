    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def is_prime(n: int) -> bool:
    """ Return True if given number is a prime number, False otherwise.
    >>> is_prime(100)
    False
    >>> is_prime(7)
    True
    >>> is_