import math
def triangle_area(r: float):
  if r < 0:
    return None
  else:
    return (1/2) * r**2 * math.pi