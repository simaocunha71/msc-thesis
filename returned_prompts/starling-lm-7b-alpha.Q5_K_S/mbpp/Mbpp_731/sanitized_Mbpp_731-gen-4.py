from math import pi, sqrt
def lateralsurface_cone(r, h):
    return pi * r * sqrt(h * h + r * r)