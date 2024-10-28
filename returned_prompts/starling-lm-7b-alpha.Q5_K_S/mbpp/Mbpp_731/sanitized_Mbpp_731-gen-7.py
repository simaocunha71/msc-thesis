import math
def lateralsurface_cone(r, h):
    """
    lateralsurface_cone(r, h) -> float

    Calculate the lateral surface area of a cone with radius r and height h.
    """
    return math.pi * r * (r + (math.sqrt(h * h + r * r)))