"""
def count_Primes_nums(num):
    if num < 2:
        return 0
    primes = [True] * (num + 1)
    primes[0], primes[1] = False, False
    for i in range(2, num + 1):
        if primes[i]:
            for j in range(i*i, num+1, i):
                primes[j] = False
    return primes.count(True)
"""

