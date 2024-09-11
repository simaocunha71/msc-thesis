To check whether a number is a perfect square or not, we can use the following steps:

1. Calculate the square root of the number using the `math.sqrt()` function.
2. Round the square root to the nearest integer using the `round()` function.
3. Square the rounded square root and compare it to the original number. If they are equal, the number is a perfect square. If not, the number is not a perfect square.

Here's an example implementation of the `is_perfect_square()` function:

```python
import math

def is_perfect_square(n):
    root = math.isqrt(n)  # This function is available in Python 3.8 and later. For older versions, use math.sqrt(n) and round(math.sqrt(n))
    return root * root == n
```

You can use this function to check whether a number is a perfect square or not. For example, `is_perfect_square(10)` will return `False` because 10 is not a perfect square, while `is_perfect_square(9)` will return `True` because 9 is a perfect square.

The `math.isqrt()` function is used to calculate the integer square root of a number. It rounds the result to the nearest integer towards zero. This function is available in Python 3.8 and later. For older versions of Python, you can use the `math.sqrt()` function to calculate the square root and `round()` function to round it to the nearest integer.

It's worth noting that the `math.isqrt()` function is not available in older versions of Python. If you are using Python 3.7 or earlier, you can use the following code to implement the `is_perfect_square()` function:

```python
import math

def is_perfect_square(n):
    root = round(math.sqrt(n))
    return root * root == n
```

This code will give you the same result as the previous implementation, but it uses the `math.sqrt()` function to calculate the square root and the `round()` function to round it to the nearest integer.

To check whether a number is