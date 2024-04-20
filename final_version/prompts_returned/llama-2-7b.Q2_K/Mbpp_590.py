"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""
import math
def polar_rect(r, theta):
    x=math.sqrt(r*math.cos(theta))
    return (x, r*(1.-math.sin(theta)))

# Tests
print(polar_rect(-3, 2.0/3) == ((4+2.62679e-05j), -2.0/3))
