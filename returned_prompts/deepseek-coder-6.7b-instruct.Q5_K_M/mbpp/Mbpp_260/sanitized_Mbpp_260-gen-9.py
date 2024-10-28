import sympy
def newman_prime(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    primes = []
    num = 2
    while len(primes) < n:
        if sympy.isprime(num):
            primes.append(num)
        num += 1

    return primes[-1]