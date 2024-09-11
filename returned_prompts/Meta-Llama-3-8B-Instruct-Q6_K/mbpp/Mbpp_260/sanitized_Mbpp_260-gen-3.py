def newman_prime(n):
    primes = []
    i = 2
    while len(primes) < n:
        if all(i%p for p in primes):
            primes.append(i)
    return primes[-1] + 1