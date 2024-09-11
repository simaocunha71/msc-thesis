Here's a step-by-step guide to solve this problem:

Firstly, we can use the formula for the surface area of a sphere, which is 4 times pi times the radius squared:

surface_area = 4 * pi * radius^2

We can use the math.isclose function to check that the result is correct:

assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)

Here's a Python implementation of the surfacearea_sphere function:

import math

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

You can use this function to calculate the surface area of a sphere with a given radius. The function returns the surface area as a float value.

To use this function, you can call it with a radius value, like surfacearea_sphere(10), and it will return the surface area of a sphere with a radius of 10. You can then use the math.isclose function to check that the result is correct, like math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001).

This will check if the result of surfacearea_sphere(10) is within a relative tolerance of 0.001 of the expected result of 1256.6370614359173. If the result is within this tolerance, the assertion will pass and the program will continue without raising an exception.

Overall, this implementation allows you to calculate the surface area of a sphere with a given radius and check that the result is correct within a relative tolerance.

Here's an example of how to use this function:

import math

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)

