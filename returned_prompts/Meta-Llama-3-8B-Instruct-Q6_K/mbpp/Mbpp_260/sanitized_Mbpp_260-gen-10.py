def newman_prime(n):
    primes = [True for _ in range(2*10**6+1)]
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= 2*10**6+1:
        if primes[p]:
            for i in range(p**2, 2*10**6+1, p):
                primes[i] = False
        p += 1
    count = 0
    for p in range(2, 2*10**6+1):
        if primes[p]:
            count += 1
            if count == n:
                return p
    return None