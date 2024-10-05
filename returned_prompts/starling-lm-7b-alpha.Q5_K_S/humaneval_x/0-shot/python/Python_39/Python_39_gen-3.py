

def prime_fib(n: int):
    fib_list = [2, 3]
    fib_number = 3
    while len(fib_list) < n:
        fib_number += fib_list[-1] + fib_list[-2]
        if is_prime(fib_number):
            fib_list.append(fib_number)
    return fib_list[-1]


def is_prime(n: int):
    """
    is_prime returns True if n is prime else False.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(5)
    True
    >>> is_prime(12)
    False
    >>> is_prime(7)
    True
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fib(n: int):
    """
    fib returns n-th number in Fibonacci series.
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    """

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_matrix(n: int):
    """
    fib_matrix returns n-th number in Fibonacci series using matrix exponentiation.
    >>> fib_matrix(1)
    1
    >>> fib_matrix(2)
    1
    >>> fib_matrix(3)
    2
    >>> fib_matrix(4)
    3
