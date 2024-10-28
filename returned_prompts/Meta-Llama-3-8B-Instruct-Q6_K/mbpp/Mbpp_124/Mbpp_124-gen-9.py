```
import cmath
import math

def angle_complex(real, imag):
    return math.degrees(cmath.phase(complex(real, imag)))
```


Explanation:
The problem is asking to write a function that takes a complex number as input and returns its angle in degrees. The angle is defined as the phase of the complex number.

The unit test `assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)` suggests that the input is a complex number in the format `(real, imag)`, where `real` is the real part and `imag` is the imaginary part.

We can use the `cmath` module to handle complex numbers in Python. The `phase` function in `cmath` module returns the phase (angle) of a complex number in radians. We can convert this angle to degrees using the `math.degrees` function.

Here is the solution:
```
import cmath
import math

def angle_complex(real, imag):
    return math.degrees(cmath.phase(complex(real, imag)))
```
This function takes two arguments `real` and `imag`, converts them to a complex number using the `complex` function, calculates the phase of the complex number using `cmath.phase`, and then converts the result to degrees using `math.degrees`. The resulting angle is returned as the output of the function.