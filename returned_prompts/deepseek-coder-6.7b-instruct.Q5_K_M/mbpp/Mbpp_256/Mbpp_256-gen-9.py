
def count_Primes_nums(n):
    primes = [False, False] + [True for _ in range(2, n)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return sum(primes)


