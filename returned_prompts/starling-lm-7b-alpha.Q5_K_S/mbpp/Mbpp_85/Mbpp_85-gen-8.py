"""
The surface area of a sphere is given by the formula 4πr².
"""

from math import pi

def surfacearea_sphere(r):
    """
    This function takes a radius (r) as an argument and returns the surface area of the sphere.
    """
    return 4 * pi * (r ** 2)

# assert surfacearea_sphere(10) == 1256.6370614359173
```

Here's a Python function to find the surface area of a sphere, given its radius:

```python
from math import pi

def surfacearea_sphere(r):
    """
    This function takes a radius (r) as an argument and returns the surface area of the sphere.
    """
    return 4 * pi * (r ** 2)
```

You can use this function by passing the radius of the sphere as an argument. The function will then return the surface area of the sphere.

For example, if you want to find the surface area of a sphere with a radius of 10, you can call the function like this:

```python
print(surfacearea_sphere(10))
```

This will output the surface area of the sphere, which should be approximately 1256.6370614359173.

The function uses the formula for the surface area of a sphere, which is 4πr². Here, r is the radius of the sphere, and π is a mathematical constant (pi) approximately equal to 3.14159.

To test the function, you can use the `assert` statement to check if the function returns the expected result. In this case, you can assert that the function should return the same result as `1256.6370614359173` when the radius is `10`.

However, since the result is an approximation, you can use the `math.isclose()` function to check if the two values are close to each other within a specified relative tolerance. In this case, the relative tolerance is set to `0.001`. If the function returns a result that is within this tolerance of