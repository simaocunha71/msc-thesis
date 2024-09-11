"""
Here is a step-by-step guide to finding the surface area of a sphere using Python:

1. First, import the math module. This module provides access to mathematical functions, constants, and types. In this case, we will be using the pi (math.pi) constant.
2. Define the function surfacearea_sphere that takes a single parameter r, which represents the radius of the sphere.
3. Inside the function, calculate the surface area of the sphere using the formula 4 * math.pi * r * r. This formula is derived from the surface area of a sphere, which is 4 times pi times the radius squared.
4. Return the calculated surface area.
5. Use the assert statement to verify the correctness of the function. The assert statement is used to check if a condition is true and raises an AssertionError if the condition is false. In this case, the condition checks if the calculated surface area of a sphere with radius 10 is approximately equal to 1256.6370614359173 with a relative tolerance of 0.001. If the condition is true, the assert statement will not raise an error.
"""

import math

def surfacearea_sphere(r):
    return 4 * math.pi * r * r

# assert surfacearea_sphere(10) == 1256.6370614359173, rel_tol=0.001

"""
The assert statement in Python is used to check if a condition is true and raises an AssertionError if the condition is false. In this case, the condition checks if the calculated surface area of a sphere with radius 10 is approximately equal to 1256.6370614359173 with a relative tolerance of 0.001. If the condition is true, the assert statement will not raise an error.
"""

"""
The math module in Python provides access to mathematical functions, constants, and types. In this case, we will be using the pi (math.pi) constant, which represents the ratio of the circumference of a circle to its diameter, approximately equal to 3.141592653589793.
"""
