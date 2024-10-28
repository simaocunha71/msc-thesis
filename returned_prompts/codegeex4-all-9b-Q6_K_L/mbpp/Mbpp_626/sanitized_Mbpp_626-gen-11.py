import math
def triangle_area(r: float) -> float:
    if r < 0:
        return None
    else:
        return (math.sqrt(3) * r ** 2) / 4