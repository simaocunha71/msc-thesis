    primes = [2, 3, 5, 7, 11, 13]
    return sum((int(n, 16) in primes) for n in num)


