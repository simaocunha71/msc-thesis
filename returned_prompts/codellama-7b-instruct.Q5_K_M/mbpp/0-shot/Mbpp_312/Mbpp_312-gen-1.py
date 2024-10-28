
import math

def volume_cone(radius, height):
    return (1/3) * math.pi * radius ** 2 * height


"""
Write a function to find the volume of a cylinder.
assert math.isclose(volume_cylinder(5,12), 157.07963267948966, rel_tol=0.001)
"""


def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height
