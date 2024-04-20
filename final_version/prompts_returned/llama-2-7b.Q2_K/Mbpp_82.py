"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""
from math import sqrt, pi

def volume_sphere(radius: float = 5):
    return (pi * ((radius + 1))**3)/6
    