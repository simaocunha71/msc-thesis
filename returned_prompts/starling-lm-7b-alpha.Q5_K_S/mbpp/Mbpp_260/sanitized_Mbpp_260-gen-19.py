def newman_prime(n):
    i = 1
    while True:
        if isPrime(f(i)):
            if n == 0:
                return i
            n -= 1
        i += 1
def f(i):
    return pow(2, 2 ** i, 10 ** 9 + 7)
def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True