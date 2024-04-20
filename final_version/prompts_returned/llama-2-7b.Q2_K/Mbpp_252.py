"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
import math

def convert(x):
    r, theta = _polar_to_cartesian(x)
    return r * math.cos(theta), r * math.sin(theta)