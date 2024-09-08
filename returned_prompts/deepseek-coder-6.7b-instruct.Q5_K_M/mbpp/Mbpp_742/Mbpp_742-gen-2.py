"""
The formula to calculate the area of a tetrahedron is:
Area = √3 * side^2

Here is the Python function that uses this formula:
"""
import math

def area_tetrahedron(side):
    return math.sqrt(3) * side ** 2

assert area_tetrahedron(3) == 15.588457268119894


