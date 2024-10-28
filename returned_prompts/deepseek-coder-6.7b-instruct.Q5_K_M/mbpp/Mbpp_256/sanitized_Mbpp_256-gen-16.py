def count_Primes_nums(n):
    sieve = [1] * n
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = 0
    return sum(sieve)