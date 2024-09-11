import math
def lateralsurface_cone(r, h):
    return math.pi * r * (r + math.sqrt(r**2 + h**2))