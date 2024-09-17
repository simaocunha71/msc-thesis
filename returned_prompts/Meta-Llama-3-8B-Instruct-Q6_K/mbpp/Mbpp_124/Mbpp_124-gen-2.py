```
import math

def angle_complex(real, imag):
    return math.atan2(imag, real)
```


The problem is asking for a function that takes a complex number as input and returns its angle in radians. The input complex number is represented as a pair of real and imaginary parts.

The unit test `assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)` suggests that the input complex number is an instance of the built-in complex type in Python, which represents complex numbers with a real and imaginary part.

The `math.atan2` function is used to calculate the angle of the complex number. This function takes two arguments, `y` and `x`, and returns the angle in radians from the positive x-axis to the point `(x, y)`. It is used in this case with the imaginary and real parts of the complex number as arguments.

Here is the solution:
```
import math

def angle_complex(real, imag):
    return math.atan2(imag, real)
```
This function takes two arguments, `real` and `imag`, which are the real and imaginary parts of the complex number. It returns the angle of the complex number in radians using the `math.atan2` function. The `math.isclose` function is used in the unit test to check if the result is close to the expected value. The `rel_tol` argument is set to 0.001 to allow for a small tolerance in the comparison.