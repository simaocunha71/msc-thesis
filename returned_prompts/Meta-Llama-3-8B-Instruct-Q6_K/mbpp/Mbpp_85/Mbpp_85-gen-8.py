```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```


This problem is asking you to write a function that calculates the surface area of a sphere given its radius. The surface area of a sphere is given by the formula `4 * pi * r^2`, where `r` is the radius of the sphere.

The unit test provided helps to clarify the problem by showing an example of how the function should behave. The test checks that the function returns the correct surface area for a sphere with a radius of 10.

Here is a Python solution for the problem:
```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```
This function takes a radius as input, calculates the surface area using the formula, and returns the result. The `math.pi` constant is used to get the value of pi, and the `**` operator is used to raise the radius to the power of 2. The result is then returned by the function.