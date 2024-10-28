import math
def triangle_area(radius: int) -> float:
  if radius <= 0:
    return None
  return (math.pi * radius ** 2) / 2