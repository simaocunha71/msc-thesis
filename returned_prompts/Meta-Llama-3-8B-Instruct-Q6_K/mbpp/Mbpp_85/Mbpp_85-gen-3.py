```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```


In this problem, we need to write a function that calculates the surface area of a sphere given its radius. The surface area of a sphere is given by the formula 4 * pi * r^2, where r is the radius of the sphere.

The unit test provided in the problem ensures that our function is working correctly. The test checks if the surface area of a sphere with a radius of 10 is approximately equal to 1256.6370614359173.

Here is the solution in Python:
```
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * (radius ** 2)
```
This function takes the radius of the sphere as input and returns its surface area. The math.pi constant is used to calculate the value of pi, which is approximately 3.14159. The ** operator is used to raise the radius to the power of 2. The function returns the result of the calculation, which is the surface area of the sphere.