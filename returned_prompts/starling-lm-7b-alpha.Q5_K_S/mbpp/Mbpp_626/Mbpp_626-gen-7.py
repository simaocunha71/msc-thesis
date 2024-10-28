
import math
def triangle_area(r: int) -> float:
  if r < 0:
    return None
  else:
    return (r * r * math.sqrt(3)) / 4


