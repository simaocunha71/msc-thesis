"""
To find the surface area of a sphere, we need to use the formula:
Surface Area = 4 * pi * r^2
Here, r is the radius of the sphere.
"""

import math

def surfacearea_sphere(r):
    return 4 * math.pi * r**2

# Test the function
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)

"""
Here, we first import the math module to use the pi value. Then, we define the function surfacearea_sphere(r) that takes the radius as an argument. Inside the function, we calculate the surface area using the formula and return the result.
Finally, we test the function by passing a value of 10 for the radius and checking if the result is close to the expected value of 1256.6370614359173 within a relative tolerance of 0.001 using the math.isclose() function.
"""

# Here are some additional notes about the math module and the math.isclose() function:

# The math module in Python contains various mathematical functions and constants. It is imported using the import keyword.

# The math.isclose() function is used to check if two numbers are approximately equal within a given relative tolerance. It returns True if the absolute difference between the two numbers is less than or equal to the product of the relative tolerance and the larger of the two numbers, and False otherwise.

# The relative tolerance is a non-negative number that specifies the maximum allowable difference between the two numbers. It is usually expressed as a fraction of the larger number.

# In the given test case, we set the relative tolerance to 0.001, which means we consider two numbers to be approximately equal if their absolute difference is less than or equal to 0.001 times the larger of the two numbers.

# The math.isclose() function is particularly useful in numerical computations where small differences can be significant, such as in this problem where we are dealing with the surface area of a sphere.

"""
In the above code, we import the math module to use the pi value. We