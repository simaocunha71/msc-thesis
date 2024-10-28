from math import pi, sqrt
def lateralsurface_cone(r,h):
    """
    Returns the lateral surface area of a cone with radius r and height h.
    """
    return pi * r * (r + (h*sqrt(h*h + r*r)))