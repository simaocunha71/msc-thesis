Here is the Python solution:

```Python
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors = set()
    for i in range(2, a + 1):
        if a % i == 0 and is_prime(i):
            prime_factors.add(i)
        if len(prime_factors) > 3:
            break

    return len(prime_factors) == 3
```

This function `is_multiply_prime` checks if the given number `a` is the multiplication of 3 prime numbers. It does this by first defining a helper function `is_prime` to check if a number is prime. It then checks all numbers from 2 to `a` (inclusive) to see if they are prime factors of `a`. If it finds 3 prime factors, it returns `True`; otherwise, it returns `False`. The time complexity of this function is O(sqrt(a)), and the space complexity is O(1).  Please note that this function is not optimized for large numbers, as it checks all numbers up to `a` to find the prime factors. For large numbers, you may need to use more efficient algorithms or data structures, such as the Sieve of Eratosthenes.  Also, the function will return `False` for numbers that are not less than 100, as per the problem statement.  If you want to check for numbers of any size, you can modify the function to handle that.  For example, you could add a check at the beginning of the function to return `False` if `a` is not less than 100.  Here is how you can do that:

```Python
def is_multiply_prime(a):
    if a >= 100:
        return False
    # rest of the function remains the same
```  This way, the function will return `False` for numbers greater than or equal to 100, and will check for 3 prime factors for numbers less than 100.  However, please note that this function is not optimized for large numbers, as it checks all numbers up to `a` to find the prime factors. For large numbers, you may need to use more efficient algorithms or data structures, such as the Sieve of Eratosthen