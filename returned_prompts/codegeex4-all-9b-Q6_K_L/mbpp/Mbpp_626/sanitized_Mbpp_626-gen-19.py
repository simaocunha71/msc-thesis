import math
def triangle_area(radius: float):
  if radius < 0:
    return None
  else:
    return (1/2) * radius * math.sqrt(2 * radius**2 - radius**2)