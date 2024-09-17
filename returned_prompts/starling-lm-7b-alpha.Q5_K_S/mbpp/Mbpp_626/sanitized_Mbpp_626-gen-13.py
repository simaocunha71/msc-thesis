import math
def triangle_area(r: float) -> float:
  if r < 0:
    return None
  else:
    return (math.pi * r ** 2) / 2