

def prime_fib(n: int):
    def fib(n: int):
        if n < 2:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    while True:
        if fib(n) > 0 and is_prime(fib(n)):
            return fib(n)
        else:
            n += 1


def is_prime(n: int):
    """
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(17)
    True
    >>> is_prime(10)
    False
    >>> is_prime(100)
    False
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Test
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89



















































































































































































