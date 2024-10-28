```
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)
```
The problem is asking to create a function that calculates the volume of a sphere given its radius. The formula for the volume of a sphere is (4/3) * π * r^3, where r is the radius of the sphere.

The unit test provided ensures that the function works correctly by comparing the result with the expected value for a sphere with a radius of 10. The `math.isclose` function is used to compare the results because the actual result might not be exactly equal to the expected value due to floating point precision issues. The `rel_tol` parameter is set to 0.001 to allow a small relative difference between the results.

The function `volume_sphere` takes a single argument `radius` and returns the volume of the sphere with that radius. It uses the formula mentioned above to calculate the volume and returns the result.