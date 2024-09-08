def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(primes) - 2  # subtract 2 because we start from 0 and 1