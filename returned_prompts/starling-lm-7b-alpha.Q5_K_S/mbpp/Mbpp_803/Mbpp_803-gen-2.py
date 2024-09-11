To check whether a given number is a perfect square or not, we can follow these steps:

1. Calculate the square root of the number using the `math.sqrt()` function.
2. Round the square root to the nearest integer using the `round()` function.
3. Calculate the square of the rounded square root.
4. If the rounded square root is equal to the square of the rounded square root, then the number is a perfect square. Otherwise, it is not.

Here is the Python code that implements these steps:

```python
import math

def is_perfect_square(num):
    if num < 0:
        return False
    square_root = math.isqrt(num)
    return square_root * square_root == num
```

You can use this function to check if a number is a perfect square. For example:

```python
print(is_perfect_square(10))  # False
print(is_perfect_square(25))  # True
```

Note that the `math.isqrt()` function is used to calculate the integer square root of a number. It is available in Python 3.8 and later versions. If you are using an older version of Python, you can use the `round()` function to round the square root to the nearest integer, and then calculate the square of the rounded square root as shown in the code above.

Also note that the function returns `False` if the given number is less than 0, as a negative number cannot be a perfect square.

"""

def is_perfect_square(num):
    if num < 0:
        return False
    square_root = math.isqrt(num)
    return square_root * square_root == num
```