```
import cmath
import math

def angle_complex(real, imag):
    return math.degrees(cmath.phase(complex(real, imag)))
```



Here is how you can use this function:

```
print(math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001))
```



Explanation:

This function uses the cmath module to create a complex number from the given real and imaginary parts. The cmath.phase function is then used to get the phase angle of the complex number, which is equivalent to the angle. The math.degrees function is used to convert the phase angle from radians to degrees.

The unit test provided is:

```
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
```

This test checks if the angle of the complex number 0 + 1j is approximately equal to 1.5707963267948966 radians (or 90 degrees), which is the expected result. The rel_tol parameter is set to 0.001, which means the test will pass if the result is within 0.1% of the expected value.