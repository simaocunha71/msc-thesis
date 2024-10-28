from math import pi
def triangle_area(radius):
    if radius < 0:
        return None
    else:
        return (2 * pi * radius ** 2) / 3