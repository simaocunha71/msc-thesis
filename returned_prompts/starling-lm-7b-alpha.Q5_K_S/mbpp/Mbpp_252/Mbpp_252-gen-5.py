```
import math

def convert(complex_number):
    real_part = complex_number.real
    imaginary_part = complex_number.imag
    radius = math.sqrt(real_part ** 2 + imaginary_part ** 2)
    angle = math.atan(imaginary_part / real_part)
    if angle < 0:
        angle += math.pi
    return (radius, angle)
```

Explanation:
The function `convert` takes a complex number as input and returns its polar coordinates as a tuple `(radius, angle)`. The radius is calculated using the Pythagorean theorem, and the angle is calculated using the arctangent function.

To test the function, you can use the assertion `assert convert(1) == (1.0, 0.0)`. This asserts that when the function is called with the complex number `1`, it should return the polar coordinates `(1.0, 0.0)`.

It's important to note that the angle returned by the function is in radians, not degrees.

The function is implemented in Python, but it can be easily adapted to other programming languages as well.

In Python, the `math` module provides the necessary mathematical functions for calculating the radius and angle in polar coordinates.

The `convert` function is a simple implementation of the conversion from complex numbers to polar coordinates. It can be further improved by adding error handling and validation for the input complex number.
```

```
