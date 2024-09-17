
def count_Primes_nums(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    return sum(primes)


