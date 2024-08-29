def count_Primes_nums(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(n):
        if is_prime(i):
            count += 1
    return count

print(count_Primes_nums(5))  # 2

# Optimized Solution
def count_Primes_nums_optimized(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

print(count_Primes_nums_optimized(5))  # 2

# More Optimized Solution using Sieve of Eratosthenes
def count_Primes_nums_Sieve(n):
    primes = [True] * n
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1

    count = 0
    for i in range(2, n):
        if primes[i]:
            count += 1
    return count

print(count_Primes_nums_Sieve(5))  # 2
<jupyter_output>
2
2
2
<jupyter_text>
**Problem 2**Given two strings s and t, determine if they are isomorphic.Two strings are isomorphic if the characters in s can be replaced to get t.All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.Example 1:Input: s = "egg", t = "add"Output: true