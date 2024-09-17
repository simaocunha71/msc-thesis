import math
def lateralsurface_cone(r,h):
    if r <= 0 or h <= 0:
        return "Input values should be positive"
    else:
        return math.pi * r * (r + math.sqrt(h**2 + r**2))