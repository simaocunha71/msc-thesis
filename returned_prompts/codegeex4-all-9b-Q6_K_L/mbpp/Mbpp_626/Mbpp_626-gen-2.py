import math
def triangle_area(radius: int) -> float:
  if radius <= 0:
    return None
  else:
    return (math.pi * radius * radius) / 2

