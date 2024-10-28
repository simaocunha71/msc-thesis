import math
def lateralsurface_cone(r: float, h: float) -> float:
    return math.pi * r * (r + (2 * h))