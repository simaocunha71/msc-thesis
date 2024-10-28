def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    p = 2
    while p * p < n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(1 for p in primes if p)