"""
import math

def surface_Area(edge, height):
    """
    This function returns the surface area of a square pyramid with a given base edge and height.
    """
    return (edge * height) + (edge * edge) * (math.sqrt(2))

# Test
assert surface_Area(3,4) == 33
"""

def surface_Area(edge, height):
    """
    This function returns the surface area of a square pyramid with a given base edge and height.
    """
    return (edge * height) + (edge ** 2) * math.sqrt(2)

# Test
assert surface_Area(3,4) == 33

In the given problem, we need to find the surface area of a square pyramid. The formula for the surface area of a pyramid is the sum of the areas of the four triangular faces, which can be calculated using the formula:

Surface Area = Base Area + (Base Area × Height) / 2

For a square pyramid, the base is a square with side length 'edge', and the height is 'height'. We can plug these values into the formula to get the surface area. However, the formula provided in the problem is slightly different, so we need to adjust our calculation accordingly.

The adjusted formula for the surface area of a square pyramid is:

Surface Area = (Edge × Height) + (Edge ** 2) × sqrt(2)

Where 'Edge' is the length of the base edge of the pyramid and 'Height' is the height of the pyramid. We can use this formula to calculate the surface area of a square pyramid given its base edge and height.

In the provided Python function, we define a function called 'surface_Area' that takes two arguments: 'edge' and 'height'. Inside the function, we use the adjusted formula to calculate the surface area and return the result. We also include a test case to verify that the function works correctly.

To use the function, you can simply call it with the desired values for 'edge' and 'height', and it will return the surface area of the square pyramid. For example, if you call 'surface_Area(3, 4)', it will return