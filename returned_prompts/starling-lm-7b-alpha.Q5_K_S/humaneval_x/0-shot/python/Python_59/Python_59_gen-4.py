
To solve this problem, we need to find the largest prime factor of a given number. We can start by defining a helper function called `is_prime` that checks if a number is prime. Then, we can use this function to find the largest prime factor.

Here's an example solution:

```python
def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(13)
    True
    >>> is_prime(12)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while not is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                n //= i
                break
    return n
```

In this solution, the `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is divisible, the function returns False, indicating that the number is not prime. If no factors are found, the function returns True, indicating that the number is prime.

The `largest_prime_factor` function uses the `is_prime` function to find the largest prime factor of the given number `n`. It starts by checking if `n` is prime itself. If it's not prime, it iterates from 2 to the square root of `n` and checks if `n` is divisible by any of these values. If it is divisible, it divides `n` by the factor and continues the loop. The loop continues