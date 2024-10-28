
The largest divisor of a number can be found by using the square root of the number. Here's a step-by-step guide on how to do it:

1. Take the square root of the number `n`. The square root of a number `n` is a number that when multiplied by itself gives `n`. For example, the square root of 9 is 3 because 3 * 3 = 9.
2. Round the square root down to the nearest whole number. The rounded down square root of a number is the largest number that can be multiplied by itself to give the original number. For example, the rounded down square root of 9 is 3 because 3 * 3 = 9.
3. This rounded down square root is the largest divisor of the original number.

Here's how you can implement it in Python:

```python
import math

def largest_divisor(n: int) -> int:
    return math.isqrt(n)
```

This code uses the `math.isqrt()` function to calculate the rounded down square root of a number. The function `math.isqrt(n)` returns the largest number that can be multiplied by itself to give `n`.

Here's an example usage of the function:

```python
print(largest_divisor(15))  # prints: 5
```

The largest divisor of 15 is 5, as 5 * 5 = 25.

Here are some additional examples of the function:

```python
print(largest_divisor(28))  # prints: 4
print(largest_divisor(100))  # prints: 10
print(largest_divisor(36))  # prints: 6
```

The largest divisor of 28 is 4 because 4 * 4 = 16. The largest divisor of 100 is 10 because 10 * 10 = 100. The largest divisor of 36 is 6 because 6 * 6 = 36.