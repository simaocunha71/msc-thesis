```
import math

def surfacearea_sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
```


The problem is asking to write a function that calculates the surface area of a sphere given its radius. The surface area of a sphere is calculated using the formula `4 * pi * r^2`, where `r` is the radius of the sphere.

The unit test `assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)` helps to verify the correctness of the function. It checks if the result of the function `surfacearea_sphere(10)` is close to the expected value `1256.6370614359173` with a relative tolerance of 0.001.

The solution is a simple Python function that takes the radius of the sphere as input and returns the calculated surface area. The `math.pi` constant is used to get the value of pi. The `**` operator is used to raise the radius to the power of 2. The result is multiplied by 4 and pi to get the surface area.