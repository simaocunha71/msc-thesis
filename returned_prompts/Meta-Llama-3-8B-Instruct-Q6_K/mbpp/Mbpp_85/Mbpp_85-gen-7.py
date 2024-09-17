```
import math

def surfacearea_sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
```



The problem is asking to write a function that calculates the surface area of a sphere given its radius. 

The surface area of a sphere can be calculated using the formula 4 * pi * r^2, where r is the radius of the sphere.

The unit test provided checks if the function surfacearea_sphere(10) returns the correct surface area for a sphere with a radius of 10. The correct surface area is approximately 1256.6370614359173. The test uses the math.isclose function to compare the result with the expected value, allowing for a small tolerance.

Here is the solution in Python:

```python
import math

def surfacearea_sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
```



This function takes a radius as input, calculates the surface area using the formula, and returns the result. The unit test provided ensures that the function works correctly for a sphere with a radius of 10. The function can be used to calculate the surface area of spheres with any radius.