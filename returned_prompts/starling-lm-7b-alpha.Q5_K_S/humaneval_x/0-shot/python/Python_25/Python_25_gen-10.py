    def _factorize(n):
        factors = []
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors.append(i)
                n = n // i
        if n > 1:
            factors.append(n)
        return factors

    return _factorize(n)


# Made by: Mukund Patel











```
# Made by: Mukund Patel

```
from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    def _factorize(n):
        factors = []
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors.append(i)
                n = n // i
        if n > 1:
            factors.append(n)
        return factors

    return _factorize(n)
```

This code defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of that integer. The function `_factorize` is a helper function that is used to calculate the prime factors. It uses a loop to iterate through all numbers from 2 to the square root of `n` (inclusive) and checks if `n` is divisible by the current number. If it is, the current number is added to the `factors` list and `n` is divided by the current number. This process continues until `n` is no longer divisible by the current number. If `n` is still greater than 1, it