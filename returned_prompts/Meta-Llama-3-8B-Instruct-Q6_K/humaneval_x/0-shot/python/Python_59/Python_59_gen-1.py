def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
# Testing the function:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

The problem is asking for a function that returns the largest prime factor of a given number. The function should only work for numbers greater than 1 and not prime.

The solution is a simple iterative algorithm that starts from 2 (the smallest prime number) and checks if it is a factor of the given number. If it is, it divides the number by the factor and continues checking for the next factor. This process continues until the number is reduced to 1. The last remaining number is the largest prime factor.

The function is tested with two examples: 13195 and 2048. The expected output for 13195 is 29 and for 2048 is 2. The function correctly returns these values.