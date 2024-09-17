import math
def triangle_area(r:float):
    if r < 0:
        return None
    else:
        return 0.5 * math.pow(r, 2) * math.pi

