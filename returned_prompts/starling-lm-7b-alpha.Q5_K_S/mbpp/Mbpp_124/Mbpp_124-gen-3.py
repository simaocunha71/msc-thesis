Here's a Python function that can be used to find the angle of a complex number:

```python
import math

def angle_complex(real, imag):
    angle = math.atan2(imag, real)
    return angle
```

The `angle_complex` function uses the `math.atan2()` function to calculate the angle. The `math.atan2()` function takes two arguments - the imaginary part and the real part of the complex number. It returns the angle in radians from the positive x-axis to the point (x,y). 

In the provided assert statement, the `angle_complex` function is tested with the complex number `0 + 1j`. The expected result is `1.5707963267948966`, which is equivalent to `90` degrees. The `math.isclose()` function is used to check if the calculated angle is close to the expected angle within a relative tolerance of `0.001`. 

The assert statement verifies that the `angle_complex` function correctly calculates the angle of the complex number. 

You can use this function to find the angle of any complex number by providing the real and imaginary parts as arguments.

```python
angle = angle_complex(real, imag)
```

where `real` and `imag` are the real and imaginary parts of the complex number, respectively. 

The function will return the angle in radians from the positive x-axis to the point (x,y). 

For example, if you want to find the angle of the complex number `3 + 4j`, you can use the function like this:

```python
angle = angle_complex(3, 4)
print(angle)
```

This will print the angle in radians from the positive x-axis to the point (3,4). 

Note that the angle is returned in radians, not degrees. If you want to convert it to degrees, you can use the `math.degrees()` function:

```python
angle_degrees = math.degrees(angle)
print(angle_degrees)
```

This will print the angle in degrees from the positive x-axis to the point