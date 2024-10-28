

def prime_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        while not is_prime(a):
            a, b = b, a+b
    return a

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        while not is_prime(a):
            a, b = b, a+b
    return a


def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        while not is_prime(a):
            a, b = b, a+b
    return a


def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_fib(n):
    a, b = 0, 1
    for _ in range(n):
