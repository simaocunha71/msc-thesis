
def newman_prime(n):
    if n == 1:
        return 2
    primes = [2]
    candidate = 3
    while len(primes) < n:
        if all(candidate % p > 0 for p in primes):
            primes.append(candidate)
        candidate += 2
    return primes[-1]


