```
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```


The function `largest_prime_factor` takes an integer `n` as input and returns the largest prime factor of `n`. The function iterates from `2` to the square root of `n`, checking if `n` is divisible by `i`. If `n` is divisible, `i` is a factor, and `n` is divided by `i`. This process continues until `i * i` exceeds `n`. The remaining value of `n` is the largest prime factor. The function assumes `n > 1` and is not a prime.

The unit tests provided in the problem statement are:
```
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
```
These tests verify that the function correctly returns the largest prime factor for the given inputs.