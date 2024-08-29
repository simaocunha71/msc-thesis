def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [1] * n
    primes[0] = primes[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = 0
    return sum(primes)

print(count_Primes_nums(5))  # 2

Explanation:
This function works by first initializing a list of ones of length n. This list will represent whether a number is prime (1) or not (0). We then loop through each number from 2 to the square root of n, and for each one, if it is prime, we loop through each multiple of that number and mark it as not prime. Finally, we return the sum of the primes list.

The reason we only need to check up to the square root of n is because a larger factor of n would be a multiple of smaller factor that has already been checked.

For example, if n = 36, the prime numbers less than 36 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31. If we didn't stop at sqrt(36), we would have counted 4 as a prime number (because 4 * 9 = 36), but 4 is not a prime number (it's divisible by 2), so we stop at sqrt(36).
"""

# Task 2
