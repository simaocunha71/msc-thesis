
import math
def triangle_area(radius: int) -> float:
  if radius <= 0:
    return None
  return (radius ** 2) * math.pi


