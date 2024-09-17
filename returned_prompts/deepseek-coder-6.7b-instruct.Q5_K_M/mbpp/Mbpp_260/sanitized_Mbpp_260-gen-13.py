def newman_prime(n):
    primes = [2, 3, 5, 7, 11, 13]
    if n <= len(primes):
        return primes[n-1]
    i = primes[-1] + 2
    while len(primes) < n:
        if all(i % p > 0 for p in primes):
            primes.append(i)
        i += 2
    return primes[-1]