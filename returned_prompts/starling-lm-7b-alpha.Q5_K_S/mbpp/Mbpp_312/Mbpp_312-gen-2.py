"""
import math

def volume_cone(r, h):
    """
    Find the volume of a cone.
    """
    return math.pi * r * r * h / 3

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)

"""

