```
import math

def surfacearea_sphere(radius):
    area = 4 * math.pi * (radius ** 2)
    return area
```


The problem is asking to write a function that calculates the surface area of a sphere. The surface area of a sphere is given by the formula 4 * π * r^2, where r is the radius of the sphere.

The unit test provided is `assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)`, which means the function should return the surface area of a sphere with a radius of 10 units. The expected result is 1256.6370614359173, and the tolerance is 0.001.

Here's the solution:
```
import math

def surfacearea_sphere(radius):
    area = 4 * math.pi * (radius ** 2)
    return area
```
This function takes the radius of the sphere as input, calculates the surface area using the formula, and returns the result. The `import math` statement is needed to use the `math.pi` constant. The `**` operator is used to raise the radius to the power of 2. The `return` statement returns the calculated surface area.