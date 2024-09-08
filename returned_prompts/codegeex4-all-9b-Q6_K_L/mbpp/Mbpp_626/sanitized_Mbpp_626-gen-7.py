import math
def triangle_area(radius):
    if radius < 0:
        return None
    return (radius ** 2) * math.sin(math.pi / 2)