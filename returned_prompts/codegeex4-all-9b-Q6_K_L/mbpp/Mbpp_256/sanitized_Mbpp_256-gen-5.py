def count_Primes_nums(num):
    if num <= 2:
        return 0
    primes = [True] * num
    primes[0], primes[1] = False, False
    for i in range(2, int(num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, num, i):
                primes[j] = False
    return sum(primes)