import math
def triangle_area(r):
    if r < 0:
        return None
    elif r == 0:
        return 0
    else:
        return (math.pi * r**2) / 4