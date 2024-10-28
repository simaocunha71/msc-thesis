
def newman_prime(n):
    primes = [2, 3, 5]
    yield_primes = lambda x: all(x % p > 0 for p in primes)
    x = primes[-1] + 2
    while len(primes) < n:
        if yield_primes(x):
            primes.append(x)
        x += 2
    return primes[-1]


