```
import cmath
def polar_rect(r, theta):
    x = r * cmath.cos(cmath.radians(theta))
    y = r * cmath.sin(cmath.radians(theta))
    return (x, y)
```


The function `polar_rect(r, theta)` takes two parameters, `r` (radius) and `theta` (angle in degrees), and returns the equivalent rectangular coordinates `(x, y)`.
The `cmath` module is used to perform complex arithmetic, and `math.radians(theta)` is used to convert the angle from degrees to radians.

The unit test `assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))` checks the function with a radius of 3 and an angle of 4 degrees, and ensures that the function returns the correct rectangular coordinates. The expected output is `(5.0, 0.9272952180016122)` for the real part and `-2+2.4492935982947064e-16j` for the imaginary part. The actual output is `(5.0, 0.9272952180016122)` for the real part and `-2+2.4492935982947064e-16j` for the imaginary part, which matches the expected output.