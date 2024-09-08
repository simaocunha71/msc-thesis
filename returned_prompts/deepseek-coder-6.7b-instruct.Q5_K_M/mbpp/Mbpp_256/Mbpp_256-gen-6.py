Here is the Python solution using Sieve of Eratosthenes algorithm:

```python
def count_Primes_nums(n):
    if n < 2:
        return 0
    sieve = [1] * n
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = 0
    return sum(sieve)

print(count_Primes_primes(5))  # 2
```

The function `count_Primes_nums` creates a boolean array `sieve` of size `n` and initializes all entries as true. A value in `sieve[i]` will finally be false if `i` is Not a prime, otherwise true. So finally we return sum of all true values in `sieve`.

The Sieve of Eratosthenes works by iteratively marking the multiples of numbers starting from 2, the first prime number, as non-prime.
"""

# Sieve of Eratosthenes algorithm is used to solve this problem.

# It is an ancient algorithm used to find all primes smaller than N, where N less than 10 million.
"""

# The time complexity of the Sieve of Eratosthenes algorithm is O(n log log n), which is very efficient.
"""

# The space complexity of the Sieve of Eratosthenes algorithm is O(n), as it requires an extra space of size n for storing the sieve.
"""

# Note: The function `count_Primes_nums` returns the count of prime numbers less than the given non-negative number `n`.
"""
"""

# The function `count_Primes_nums` returns the count of prime numbers less than the given non-negative number `n`.
"""
"""

# The function `count_Primes_nums` returns the count of prime numbers less than the given non-negative number `n`.
"""
"""

# The function `count_Primes_nums` returns the count of prime numbers