```python


def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(x: int) -> bool:
        """Return True if x is a prime number, else False."""
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    largest_factor = None
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor

```
