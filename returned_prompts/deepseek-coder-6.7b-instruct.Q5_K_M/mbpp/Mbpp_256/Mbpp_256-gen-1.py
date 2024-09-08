Here is the python function that solves the problem:

```python
def count_Primes_nums(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sum(sieve)

assert count_Primes_primes(5) == 2
```

This function works by using the Sieve of Eratosthenes algorithm to find all prime numbers up to the given number. It starts by assuming all numbers are prime (True). It then iteratively marks the multiples of each found prime number as composite (False). Finally, it sums up the number of True values in the list, which gives the count of prime numbers.
"""

# 5. Write a Python function that takes in a string and returns the string reversed.
