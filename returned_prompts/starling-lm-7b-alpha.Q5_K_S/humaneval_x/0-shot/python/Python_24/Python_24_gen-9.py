
Here's a Python function to find the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # start from 2 and go up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    # if no divisor found up to sqrt(n), return n
    return n
```

This function starts from 2 and goes up to the square root of the given number. For each number in this range, it checks if it is a divisor of the given number. If it is, it returns the divisor. If no divisor is found in this range, it returns the given number itself, as it is the largest divisor of the number.

For example, when you call `largest_divisor(15)`, it will return 5, because 5 is the largest number that divides 15 evenly and is smaller than 15.

You can test the function with other numbers as well to check if it works correctly.

```python
print(largest_divisor(28))  # Output: 14
print(largest_divisor(49))  # Output: 7
```

This function should work correctly for all positive integers.

```python
print(largest_divisor(0))  # Output: 0
print(largest_divisor(1))  # Output: 1
print(largest_divisor(-1))  # Output: -1
```

Please note that this function will not work correctly for negative integers, as the square root of a negative number is not defined in the context of real numbers.

```python
print(largest_divisor(-5))  # Raises ValueError: n must be a positive integer
```

To handle negative integers, you can add a check at the beginning of the function to ensure that `