

from math import sqrt, floor

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    def is_prime(n: int):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def fib(n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def is_fib_prime(n: int):
        if n < 2:
            return False
        a, b = 5, 8
        while a <= n:
            if a == n:
                return True
            b = a + b
            a = b - a
        return False

    count = 0
    while count < n:
        num = fib(count)
        if is_fib_prime(num):
            count += 1
        else:
            count += 1
    return num
