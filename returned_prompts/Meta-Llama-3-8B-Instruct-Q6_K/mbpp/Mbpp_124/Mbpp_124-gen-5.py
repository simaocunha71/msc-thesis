```
import cmath
def angle_complex(real, imag):
    return cmath.phase(complex(real, imag))
```


This function uses the `cmath.phase` function to get the phase (angle) of a complex number. The `cmath` module provides functions for working with complex numbers. The `complex` function is used to create a complex number from the given real and imaginary parts. The `phase` function returns the phase (angle) of the complex number in radians. The `assert` statement is used to test the function with the input `(0, 1j)` and compare the result with the expected angle of `π/2` (approximately `1.5707963267948966`). The `math.isclose` function is used to compare the result with the expected value due to floating point precision errors. The `rel_tol` parameter is set to `0.001` to allow for a small tolerance in the comparison.