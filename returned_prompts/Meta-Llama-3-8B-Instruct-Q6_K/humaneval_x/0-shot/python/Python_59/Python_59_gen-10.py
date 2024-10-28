```
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Start with the largest possible prime factor, which is n // 2
    for i in range(n // 2, 1, -1):
        # Check if i is a prime factor
        if n % i == 0:
            # Check if i is a prime number
            if is_prime(i):
                return i

def is_prime(m: int) -> bool:
    """Return True if m is a prime number."""
    if m <= 1:
        return False
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            return False
    return True
```
This code defines two functions: `largest_prime_factor` and `is_prime`. The `largest_prime_factor` function finds the largest prime factor of a given integer `n`. It does this by iterating from `n // 2` down to 1, checking each number to see if it is a prime factor of `n`. If it is, it checks if the number is prime using the `is_prime` function. If it is prime, it returns the number as the largest prime factor.

The `is_prime` function checks if a given integer `m` is prime. It does this by checking if `m` is less than or equal to 1 (in which case it is not prime), or if it has any divisors other than 1 and itself (in which case it is not prime). If `m` passes these tests, it is considered a prime number.

The `largest_prime_factor` function is tested with the examples provided in the problem statement. The first example, `largest_prime_factor(13195)`, returns 29, which is the largest prime factor of 13195. The second example, `largest_prime_factor(2048)`, returns 2, which is the largest prime factor of 2048.