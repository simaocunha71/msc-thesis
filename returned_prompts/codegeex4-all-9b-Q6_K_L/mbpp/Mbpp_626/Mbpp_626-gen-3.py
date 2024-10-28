import math
def triangle_area(radius: float) -> float:
  if radius < 0:
    return None
  else:
    return 0.5 * radius**2 * math.pi

