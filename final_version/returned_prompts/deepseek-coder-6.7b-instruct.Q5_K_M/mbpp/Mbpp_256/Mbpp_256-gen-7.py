def count_Primes_nums(n):
    if n<2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i, is_prime in enumerate(sieve):
        if is_prime:
            for n in range(i*i, n, i):
                sieve[n] = False
    return sieve.count(True)

print(count_Primes_nums(5))

# Output: 2


Explanation:
The function works by creating a boolean list of length 'n' where each value is initially True. Then, it iteratively marks the multiples of each number starting from 2 as False (non-prime). At the end, it counts the number of True values in the list (prime numbers).
"""
Here, we use the Sieve of Eratosthenes algorithm to solve this problem. It is one of the most efficient ways to find all primes smaller than 'n' when 'n' is smaller than 10 million.
"""

"""
We start by assuming that every number is prime. We then iterate from 2 to sqrt(n) and for each number, if it is prime, we mark all its multiples as not prime. The reason we only need to mark multiples up to sqrt(n) is because a larger multiple of the number would have already been marked not prime by a smaller number.
"""

"""
Finally, we count the number of True values in the list and return this count.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
