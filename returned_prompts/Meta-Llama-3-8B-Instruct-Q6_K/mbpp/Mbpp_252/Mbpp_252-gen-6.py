You can solve this problem as follows:

```python
import math
def convert(c):
    if c.real == 0:
        return (0, 0)
    else:
        magnitude = math.sqrt(c.real**2 + c.imag**2)
        angle = math.atan2(c.imag, c.real)
        return (magnitude, math.degrees(angle))
```



Here is a Python function that converts complex numbers to polar coordinates. The `math.atan2` function is used to calculate the angle in radians, and then the `math.degrees` function is used to convert the angle to degrees. This is necessary because the problem statement asks for the angle in degrees. If the real part of the complex number is zero, then the function returns (0, 0) as the polar coordinates.

The unit test `assert convert(1) == (1.0, 0.0)` is passed by this function. This test checks that the function correctly converts the complex number 1 (which is equivalent to 1 + 0j in Python) to the polar coordinates (1, 0) which represents a point on the positive real axis. The test also checks that the angle is in degrees. The `math.atan2` function returns the angle in radians, so we need to convert it to degrees using `math.degrees`. This is why the expected output is `(1.0, 0.0)` instead of `(1, 0)`.

Please note that this function does not handle the case where the input is not a complex number. It will raise an error if the input is not a complex number. You may want to add error handling code to handle this case.