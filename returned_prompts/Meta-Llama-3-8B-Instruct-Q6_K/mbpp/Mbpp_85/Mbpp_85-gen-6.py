```
import math

def surfacearea_sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
```


The surface area of a sphere is given by the formula 4πr^2, where r is the radius of the sphere. The function `surfacearea_sphere` takes a radius as input and returns the surface area. The `math.isclose` function is used to check if the calculated surface area is close to the expected value. The `rel_tol` parameter is set to 0.001 to allow for a small margin of error.

This solution passes the provided unit test. The test checks if the calculated surface area of a sphere with a radius of 10 is close to the expected value. The `math.isclose` function is used to compare the two values, allowing for a small margin of error. The test passes if the difference between the calculated and expected values is less than or equal to the specified tolerance.