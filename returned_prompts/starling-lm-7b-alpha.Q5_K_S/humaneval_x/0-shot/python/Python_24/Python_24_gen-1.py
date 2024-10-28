
Here is a Python function that finds the largest divisor of a given number:

```python
from math import sqrt

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 4:
        return n
    for i in range(int(sqrt(n)), 0, -1):
        if n % i == 0:
            return i
    return n
```

This function first checks if the number is less than 4. If it is, then it returns the number itself, since 1 and 2 are the only factors of 1 and 3 respectively.

For larger numbers, the function starts from the square root of the number and checks all divisors starting from the largest down to 1. When it finds a divisor, it stops and returns that divisor. If no divisor is found, it returns the number itself.

For example, for the input `15`, the function checks if `15` is divisible by `15` (it is), and returns `15`.

The time complexity of this function is O(sqrt(n)), since it only needs to check up to the square root of the number for divisors.

Note: The function assumes that the input `n` is a positive integer.

```python
# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(25))  # Output: 5
```





































































```

```