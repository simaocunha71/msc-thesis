import math
def lateralsurface_cone(r, h):
    return math.pi * r * (r + math.sqrt(h**2 + r**2))
    # result = 3.14159 * r * (r + math.sqrt(h**2 + r**2))  # for 3 decimal places