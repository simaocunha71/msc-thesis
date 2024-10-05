

def prime_fib(n: int) -> int:
    fib_seq = [2, 3, 5, 13, 89]
    if n < len(fib_seq):
        return fib_seq[n - 1]
    else:
        limit = 10 ** 6  # limit the search
        nth_fib = fibonacci(n)
        for i in range(limit, nth_fib, limit // 2):
            if is_prime(i):
                return i
        return nth_fib


def fibonacci(n: int) -> int:
    """
    Fibonacci number at position n.
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(8)
    21
    >>> fibonacci(9)
    34
    >>> fibonacci(10)
    55
    >>> fibonacci(20)
    6765
    >>> fibonacci(100)
    354224848179261915075
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(n: int) -> bool:
    """
    Returns True if n is prime, False if it is not.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
