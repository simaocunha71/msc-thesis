from math import pi
def triangle_area(radius):
    if radius < 0:
        return None
    else:
        return (radius ** 2) * pi / 2