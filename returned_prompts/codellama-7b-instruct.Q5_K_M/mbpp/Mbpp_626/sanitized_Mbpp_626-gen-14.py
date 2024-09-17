import math
def triangle_area(radius):
    if radius < 0:
        return None
    area = (radius ** 2) * (math.sqrt(3)) / 2
    return area