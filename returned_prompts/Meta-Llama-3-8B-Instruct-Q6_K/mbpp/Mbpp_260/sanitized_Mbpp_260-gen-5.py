def newman_prime(n):
    primes = []
    p = 2
    while len(primes) < n:
        if all(p % i for i in range(2, int(p**0.5) + 1)):
            primes.append(p)
        p += 1
    return primes[-1]  # Return the nth Newman-Shanks-Williams prime number