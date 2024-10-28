import math
def triangle_area(r: int) -> float:
    if r < 0:
        return None
    return (math.sqrt(3) / 4) * r ** 2