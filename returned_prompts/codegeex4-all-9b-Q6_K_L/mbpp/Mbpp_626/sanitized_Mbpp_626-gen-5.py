from math import sqrt
def triangle_area(r):
    if r < 0:
        return None
    return (r ** 2) * sqrt(3) / 4