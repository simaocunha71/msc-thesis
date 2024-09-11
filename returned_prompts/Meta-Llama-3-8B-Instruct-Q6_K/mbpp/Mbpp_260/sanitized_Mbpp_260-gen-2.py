def newman_prime(n):
    primes = [True] * (n * 1000)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= len(primes):
        if primes[p]:
            for i in range(p * p, len(primes), p):
                primes[i] = False
        p += 1
    return p * p + 1