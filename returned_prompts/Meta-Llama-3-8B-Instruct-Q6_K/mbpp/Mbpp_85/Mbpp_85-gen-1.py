```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```


The problem is asking for a function that calculates the surface area of a sphere, given its radius. The surface area of a sphere is calculated using the formula `4 * pi * r^2`, where `r` is the radius of the sphere.

The unit test `assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)` helps to verify the correctness of the function. It checks if the surface area of a sphere with a radius of 10 is approximately equal to 1256.6370614359173.

Here's the solution:
```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```
This function takes a radius as input, calculates the surface area using the formula, and returns the result. The `math.pi` constant is used to get the value of pi. The `**` operator is used to raise the radius to the power of 2. The result is multiplied by 4 and the value of pi to get the surface area.