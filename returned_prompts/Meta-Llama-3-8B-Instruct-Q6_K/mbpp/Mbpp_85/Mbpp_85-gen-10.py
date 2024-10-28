```
import math

def surfacearea_sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
```


This problem is asking to write a function that calculates the surface area of a sphere given its radius. The surface area of a sphere can be calculated using the formula 4 * π * r^2, where r is the radius of the sphere.

The unit test provided helps to clarify the expected output of the function. It checks that the surface area of a sphere with a radius of 10 is approximately 1256.6370614359173.

Here is a Python solution for the problem:

```
import math

def surfacearea_sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
```

This function takes a radius as input, calculates the surface area using the formula, and returns the result. The `math` module is used to access the value of π. The `**` operator is used to square the radius. The result is returned as the surface area of the sphere.