```
import math

def surfacearea_sphere(r:float):
    return 4 * math.pi * r**2
```

The function `surfacearea_sphere` takes the radius of the sphere as a parameter and returns the surface area of the sphere using the formula `4 * pi * r^2`. The function uses the `math.pi` constant from the `math` module to calculate the surface area of the sphere.

In the provided code, the function is tested with a radius of 10. The expected result is 1256.6370614359173, which is obtained by using the `math.isclose` function to compare the calculated surface area with the expected result, with a relative tolerance of 0.001.

To use the function, you can simply call it with the desired radius of the sphere as the argument. For example, if you want to find the surface area of a sphere with a radius of 5, you can call `surfacearea_sphere(5)`. The function will return the surface area of the sphere, which you can then use as needed in your program.

Overall, the provided code defines a function to calculate the surface area of a sphere and tests it with a specific radius.



```python
def surfacearea_sphere(r:float):
    return 4 * math.pi * r**2
```

This function takes a radius as a parameter and returns the surface area of a sphere using the formula `4 * pi * r^2`. It uses the `math.pi` constant from the `math` module to calculate the surface area.

To use the function, you can call it with the desired radius of the sphere as the argument. For example, if you want to find the surface area of a sphere with a radius of 5, you can call `surfacearea_sphere(5)`. The function will return the surface area of the sphere, which you can then use as needed in your program.

The provided code also includes a test case to verify the correctness of the function. It uses the `math.isclose` function to compare the calculated surface area with the expected result, with a relative tolerance of 0.001. This ensures that the function is accurate within the specified tolerance.