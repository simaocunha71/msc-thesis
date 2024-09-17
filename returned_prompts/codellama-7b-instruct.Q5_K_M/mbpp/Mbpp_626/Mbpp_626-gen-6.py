
from math import pi, sqrt

def triangle_area(radius):
    if radius < 0:
        return None
    a = 2 * pi * radius
    b = sqrt(4 * (1 - (1/a)) - 1)
    c = a * b
    return c


