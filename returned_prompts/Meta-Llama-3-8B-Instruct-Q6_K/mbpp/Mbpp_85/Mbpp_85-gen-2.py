```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```


The problem is asking to create a function that calculates the surface area of a sphere given its radius. The surface area of a sphere is calculated using the formula 4 * π * r^2, where r is the radius of the sphere.

The unit test provided, `assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)`, helps to clarify the problem by showing the expected output for a specific input. This test ensures that the function returns the correct result for a sphere with a radius of 10.

The solution is a simple Python function that takes the radius of the sphere as input and returns its surface area. The function uses the math module to calculate the value of π. The result is calculated using the formula 4 * π * r^2.

Here is the solution:
```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```


This function will correctly calculate the surface area of a sphere given its radius. For example, `surfacearea_sphere(10)` will return approximately 1256.6370614359173, which is the expected result for a sphere with a radius of 10.