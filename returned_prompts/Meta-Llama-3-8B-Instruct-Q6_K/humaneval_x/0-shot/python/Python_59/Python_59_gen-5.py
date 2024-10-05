```
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```

This function finds the largest prime factor of `n` by dividing `n` by the smallest prime number (2) as long as `n` is divisible by 2. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime number. This process continues until `n` is reduced to its largest prime factor. The function returns this largest prime factor.