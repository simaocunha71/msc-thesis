
from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_fib(n):
    a, b = 5, 8
    while a < n:
        b = a + b
        if b == n:
            return True
        a = b - a
    return False

def prime_fib(n):
    for i in range(n):
        fib = (5 * pow(10, i - 1, 12) + 4) // 12
        if is_prime(fib) and is_fib(fib):
            return fib
    return None

print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))
