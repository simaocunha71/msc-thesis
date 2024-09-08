import math
def triangle_area(radius):
    if radius <= 0:
        return None
    else:
        return (radius ** 2 * math.sin(math.pi / 3)) / 2