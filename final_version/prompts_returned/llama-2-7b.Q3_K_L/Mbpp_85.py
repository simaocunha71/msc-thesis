"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""
from __future__ import print_function
import math

def surfacearea_sphere(R):
	return 4 * (math.pi * R**2)
