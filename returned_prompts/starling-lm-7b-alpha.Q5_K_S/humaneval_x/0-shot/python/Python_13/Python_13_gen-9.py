
Here's a Python function that implements the Euclidean algorithm to calculate the greatest common divisor of two integers:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b != 0:
        a, b = b, a % b
    return a
```

This function uses the Euclidean algorithm to calculate the greatest common divisor. It repeatedly divides `a` by `b` and updates `a` and `b` until `b` becomes zero. The final value of `a` is the greatest common divisor of the original two integers.

Here's a breakdown of how the function works:

1. The function takes two integer arguments `a` and `b`.
2. It enters a while loop that continues until `b` becomes zero.
3. Inside the loop, it updates `a` and `b` using a tuple assignment: `a, b = b, a % b`. This means that `a` becomes the value of `b` and `b` becomes the remainder of `a` divided by `b`.
4. Once `b` becomes zero, the loop exits and the function returns the final value of `a`, which is the greatest common divisor of the original two integers.

You can use this function to calculate the greatest common divisor of any two integers by calling it with the desired arguments.

For example, `greatest_common_divisor(3, 5)` returns `1`, and `greatest_common_divisor(25, 15)` returns `5`.

```python
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

```

```

```python

```

```python

```