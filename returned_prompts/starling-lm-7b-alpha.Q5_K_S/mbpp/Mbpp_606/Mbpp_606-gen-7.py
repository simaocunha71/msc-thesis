"""
def radian_degree(degrees):
    radians = degrees * (math.pi / 180)
    return radians
"""

Here is a Python program that converts degrees to radians using the `math` library's `pi` constant and the `*` operator.

```python
import math

def radian_degree(degrees):
    radians = degrees * (math.pi / 180)
    return radians
```

To test the function, you can use the `assert` statement to verify the result. For example, if you call `radian_degree(90)`, the expected result is `1.5707963267948966`. You can use the `assert` statement to check if the result is correct:

```python
assert radian_degree(90) == 1.5707963267948966
```

If the result is correct, the `assert` statement will not raise an error. Otherwise, an `AssertionError` will be raised, indicating that the result is incorrect.

This function can be used to convert degrees to radians in various applications, such as trigonometry, physics, engineering, and computer graphics.

Here are some additional examples of how to use the `radian_degree` function:

```python
print(radian_degree(0))  # Output: 0.0
print(radian_degree(45))  # Output: 0.7853981633974483
print(radian_degree(180))  # Output: 3.141592653589793
print(radian_degree(360))  # Output: 6.283185307179586
```

In each example, the `radian_degree` function takes a degree value as an argument and returns the corresponding radian value.

By using this function, you can easily convert degrees to radians in your Python programs.

Here are some additional tips for using the `radian_degree` function:
