def count_Primes_nums(n):
    if n <= 1:
        return 0

    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    return sum(1 for p in primes if p)