To check whether the given number is a perfect square or not, we can follow these steps:

1. First, calculate the square root of the given number. If the square root is an integer, then the number is a perfect square. Otherwise, it's not.
2. To calculate the square root, we can use the `math.sqrt()` function from the `math` module in Python. However, since `math.sqrt()` returns a float, we need to check if the square root is an integer. If it is, then the number is a perfect square.
3. Here's an example implementation of the `is_perfect_square()` function:

```python
import math

def is_perfect_square(n):
    root = math.sqrt(n)
    if root.is_integer():
        return True
    else:
        return False
```

In this function, we first calculate the square root of the given number `n` using `math.sqrt(n)`. Then, we use the `is_integer()` method to check if the square root is an integer. If it is, we return `True`, indicating that the number is a perfect square. Otherwise, we return `False`.

You can use the `assert` statement to verify the correctness of the function. For example, if we call `is_perfect_square(10)`, it should return `False` since 10 is not a perfect square. The `assert` statement checks if the return value is `False`, and if it is, it raises an `AssertionError` exception.

Here's an example usage of the `is_perfect_square()` function:

```python
print(is_perfect_square(16))  # Output: True
print(is_perfect_square(10))  # Output: False
```

In the first example, `is_perfect_square(16)` returns `True` because 16 is a perfect square. In the second example, `is_perfect_square(10)` returns `False` because 10 is not a perfect square.

"""

```python
import math

def is_perfect_square(n):
    root = math