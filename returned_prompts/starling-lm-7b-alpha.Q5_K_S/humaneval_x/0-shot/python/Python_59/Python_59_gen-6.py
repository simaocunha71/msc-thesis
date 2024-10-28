
Here is one possible implementation using a while loop:

```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while n % i != 0:
        i += 1
    if i*i > n:
        return i
    else:
        return largest_prime_factor(n//i)
```

Explanation:

The function `largest_prime_factor` takes an integer `n` as input and returns the largest prime factor of `n`. It uses a while loop to repeatedly divide `n` by the smallest possible divisor (initially 2) until the quotient is no longer a prime number. If the quotient is a perfect square (i.e., the square of an integer), then it is not a prime number, and the function recursively calls itself with the quotient as the new input. If the quotient is not a perfect square, then it is the largest prime factor of `n`.

For example, when `n = 13195`, the function will repeatedly divide it by 2 until it cannot be divided evenly. Then, it will move on to the next divisor (3) and continue dividing until it cannot be divided evenly again. This process continues until the quotient is no longer a perfect square, at which point the function returns the current quotient as the largest prime factor of `n`.

The time complexity of this algorithm is O(sqrt(n)), as the largest prime factor of `n` is at most the square root of `n`.

I hope this helps! Let me know if you have any more questions.

```python

```