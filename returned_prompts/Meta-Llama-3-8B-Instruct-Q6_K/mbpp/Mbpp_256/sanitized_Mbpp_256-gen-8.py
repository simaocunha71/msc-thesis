def count_Primes_nums(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return sum(primes) - 2  # subtracting 2 for 0 and 1