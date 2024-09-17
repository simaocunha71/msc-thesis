```
import cmath
import math

def convert(z):
    r = abs(z)
    theta = cmath.phase(z)
    return (r, math.degrees(theta))
```


The function `convert(z)` takes a complex number `z` as an argument and returns its polar coordinates. It calculates the modulus (r) using the `abs()` function, and the phase (theta) using the `cmath.phase()` function. The phase is in radians, so we convert it to degrees using the `math.degrees()` function. The function returns a tuple of (r, theta) representing the polar coordinates of the complex number. 

For example, the complex number 1+0j is represented as (1.0, 0.0) in polar coordinates. The unit test `assert convert(1) == (1.0, 0.0)` ensures that the function works correctly for this case. 





Note: This solution assumes that the input is a complex number. If the input is not a complex number, the function will raise an error. If you want to handle non-complex inputs, you can add error handling code to the function.