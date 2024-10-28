def count_Primes_nums(n):
    primes = [True] * n
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(primes[2:])