
import math
def triangle_area(r: int) -> float:
  if r < 0:
    return None
  else:
    area = (math.pi * r ** 2) / 3
    return area


