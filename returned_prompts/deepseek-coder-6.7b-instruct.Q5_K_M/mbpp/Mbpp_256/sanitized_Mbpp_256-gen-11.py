def count_Primes_nums(n):
    if n < 2:
        return 0
    sieve = [True] * n
    for x in range(2, int(n ** 0.5) + 1):
        if sieve[x]:
            sieve[x * x: n: x] = [False] * len(sieve[x * x: n: x])
    return sum(sieve)