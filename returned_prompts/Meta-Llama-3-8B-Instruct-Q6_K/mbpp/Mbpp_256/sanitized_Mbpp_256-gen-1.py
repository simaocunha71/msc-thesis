def count_Primes_nums(n):
    primes = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_count = 0
    for p in range(2, n):
        if primes[p]:
            prime_count += 1
    return prime_count