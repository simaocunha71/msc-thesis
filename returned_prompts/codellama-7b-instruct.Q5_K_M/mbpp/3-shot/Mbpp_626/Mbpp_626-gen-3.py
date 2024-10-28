
import math
def triangle_area(radius: float) -> float:
  if radius < 0:
    return None
  area = (radius * radius) * math.sqrt(3) / 2
  return area


