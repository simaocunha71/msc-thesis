```
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)
```
The problem is asking you to write a function that calculates the volume of a sphere given its radius. The volume of a sphere is calculated using the formula (4/3) * π * r^3, where r is the radius of the sphere.

In this solution, we define a function `volume_sphere` that takes a single argument `radius`. We then use the formula to calculate the volume and return it. The `math` module is used to get the value of π.

The unit test `assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)` checks that the function returns the correct volume for a sphere with a radius of 10. The `math.isclose` function is used to compare the result of the function with the expected result, allowing for a small tolerance in the comparison. This is necessary because floating point calculations can sometimes introduce small errors.