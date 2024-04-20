"""
Write a function to find the circumference of a circle.
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""
from math import sin, cos
def circle_circumference(r):
    if r < 0:
        raise Exception("Radius cannot be negative.")
    else:
        return r * 2 * pi

