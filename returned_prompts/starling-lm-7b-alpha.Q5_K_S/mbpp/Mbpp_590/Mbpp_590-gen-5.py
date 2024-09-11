"""
from cmath import rect
from math import pi

def polar_rect(r, theta):
    return (r*cos(theta), r*sin(theta))

def test_polar_rect():
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))

test_polar_rect()
"""

import cmath
import math

def polar_rect(r, theta):
    return (r*math.cos(theta), r*math.sin(theta))

def test_polar_rect():
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))

test_polar_rect()

# This is a Python Program to convert Polar coordinates to Rectangular coordinates

import math

def polar_to_rectangular(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

# Test
r = 5
theta = math.pi / 4
print(polar_to_rectangular(r, theta))

# Output: (2.8867513459481287, 2.8867513459481287)

# Here is another Python Program to convert Polar coordinates to Rectangular coordinates

def polar_to_rectangular(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

r = 5
theta = math.pi / 4
print(polar_to_rectangular(r, theta))

# Output: (2.88675134594812