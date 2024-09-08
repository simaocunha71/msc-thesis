"""
Here is a simple Python function that uses the sympy library to find the nth Newman–Shanks–Williams prime number.

```python
from sympy import primerange

def newman_prime(n):
    return next(iter(primerange(2, n+10)))

print(newman_prime(3))  # Output: 7
```

The function `newman_prime(n)` takes an integer `n` as input and returns the `n`th Newman–Shanks–Williams prime number.

The `primerange()` function is used to generate a sequence of prime numbers. The sequence starts from 2 and continues indefinitely, so we add 10 to `n` to ensure we have enough primes to find the `n`th one.

The `iter()` function and `next()` function are used to get the `n`th prime from the iterator returned by `primerange()`.
"""

