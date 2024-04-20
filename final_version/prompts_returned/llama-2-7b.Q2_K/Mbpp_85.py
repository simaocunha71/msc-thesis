"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""
from math import sin, cos, pi

def surfacearea_sphere(r: float):
    return r * ((2*pi) ** 0.5 - (2 * pi))
