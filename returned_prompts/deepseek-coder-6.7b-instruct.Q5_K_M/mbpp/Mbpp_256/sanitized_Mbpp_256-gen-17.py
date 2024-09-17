def count_Primes_nums(n):
    sieve = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, n, x):
                sieve[i] = False
    return sum(sieve)