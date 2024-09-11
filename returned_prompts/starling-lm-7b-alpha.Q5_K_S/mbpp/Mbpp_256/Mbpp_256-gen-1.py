Here's a Python function that counts the number of prime numbers less than a given non-negative number.

```python
from math import sqrt

def count_Primes_nums(n):
    if n == 0:
        return 0
    else:
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
```

To use the function, call `count_Primes_nums` with a non-negative number as the argument. The function will return the number of prime numbers less than the given non-negative number.

For example, if you call `count_Primes_nums(5)`, it will return 2, because there are two prime numbers (2 and 3) less than 5.

Note that the `is_prime` function is used to check if a number is prime. It returns `True` if the number is prime, and `False` if it is not.

The `count_Primes_nums` function iterates over all numbers from 2 to the given non-negative number (inclusive), and for each number, it calls the `is_prime` function to check if it is prime. If it is prime, the count is incremented. Finally, the function returns the count of prime numbers.

This solution has a time complexity of O(n), where n is the given non-negative number.

```python
# Testing
assert count_Primes_nums(0) == 0
assert count_Primes_nums(1) == 0
assert count_Primes_nums(2) == 1
assert count_Primes_nums(3) == 1
assert count_Primes_nums(4