Here is a Python function that solves the problem:

```python
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for p1 in range(2, 100):
        if not is_prime(p1):
            continue
        for p2 in range(p1, 100):
            if not is_prime(p2):
                continue
            for p3 in range(p2, 100):
                if not is_prime(p3):
                    continue
                if p1 * p2 * p3 == a:
                    return True
    return False
```

This function `is_multiply_prime(a)` checks if the number `a` is the multiplication of 3 prime numbers. It first defines a helper function `is_prime(n)` to check if a number `n` is prime. Then it iterates over all numbers from 2 to 100, checks if they are prime, and if they are, it checks if the multiplication of the current number and two other prime numbers equals `a`. If it finds such a multiplication, it returns `True`. If it doesn't find such a multiplication after checking all numbers, it returns `False`. 

Please note that this function is not very efficient because it checks all numbers up to 100 for primality. This could be improved by using a more efficient primality test or by using a sieve to precompute all prime numbers up to 100.  However, for the given constraints, this function should work correctly. 

Also, please note that the problem statement says that `a` is less than 100, but the function doesn't use this information. If `a` could be larger than 100, the function would need to be modified accordingly.  For example, it could use a sieve to precompute all prime numbers up to `a` and then check if `a` is the multiplication of 3 prime numbers.  However, since `a` is limited to 100, this optimization is not necessary. 