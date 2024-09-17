from math import pi, sqrt, atan, cos
def triangle_area(r):
    if r < 0:
        return None
    return 0.5 * r ** 2 * atan(sqrt(2) / 2)