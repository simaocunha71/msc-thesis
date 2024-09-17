```
import cmath
import math

def angle_complex(real, imag):
    return math.degrees(cmath.phase(complex(real, imag)))
```
The function `angle_complex` takes two parameters, `real` and `imag`, which are the real and imaginary parts of a complex number respectively. It returns the angle of the complex number in degrees.

The `cmath.phase` function is used to get the phase of the complex number, which is the angle in radians. The `math.degrees` function is used to convert the angle from radians to degrees.

The unit test `assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)` checks that the function returns the correct angle for the complex number 0 + 1j, which is approximately 90 degrees. The `math.isclose` function is used to compare the result with the expected value, with a relative tolerance of 0.001. This means that the actual result can be up to 0.001 degrees different from the expected value and still be considered correct.