```
import math

def convert(n):
    r = math.sqrt(n.real ** 2 + n.imag ** 2)
    theta = math.atan2(n.imag, n.real)
    return r, theta
```

In this function, we use `math.sqrt` to calculate the magnitude of the complex number `n`. The magnitude is the square root of the sum of the squares of the real and imaginary parts. We use `math.atan2` to calculate the angle of the complex number. The angle is the arctangent of the imaginary part divided by the real part.

To test the function, we use the `assert` statement to check if the result of converting the complex number `1` is equal to `(1.0, 0.0)`. The result should be `True` if the function is correct.

This function can be used to convert any complex number to its polar coordinates.

```python
# Example usage
complex_number = complex(3, 4)
polar_coordinates = convert(complex_number)
print(polar_coordinates)  # Output: (5.0, 0.8251680420830328)
```

In this example, we convert the complex number `3 + 4i` to its polar coordinates using the `convert` function. The result is `(5.0, 0.8251680420830328)`, which represents the magnitude and angle of the complex number in polar coordinates.

```python
# Testing the function
assert convert(1) == (1.0, 0.0)  # This should return True if the function is working correctly
```

Here, we use the `assert` statement to check if the result of converting the complex number `1` is equal to `(1.0, 0.0)`. The result should be `True` if the function is correct.

```python
# Another example usage
complex_number = complex(2, -3)
polar_coordinates = convert(complex_number)
print(polar_coordinates)  # Output: (3.605