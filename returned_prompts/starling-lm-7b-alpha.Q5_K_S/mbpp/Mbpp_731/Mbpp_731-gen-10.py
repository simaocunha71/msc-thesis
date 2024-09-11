"""
import math
def lateralsurface_cone(r, h):
    """
    Finds the lateral surface area of a cone given radius r and the height h.

    Parameters
    ----------
    r : int or float
        The radius of the cone.
    h : int or float
        The height of the cone.

    Returns
    -------
    float
        The lateral surface area of the cone.
    """
    pi = math.pi
    return pi * r * math.sqrt(r**2 + h**2) + r * h * math.sqrt(2)

print(lateralsurface_cone(5,12))
"""


