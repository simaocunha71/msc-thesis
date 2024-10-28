import math
def lateralsurface_cone(r: int, h: int) -> float:
  return math.pi * r * math.sqrt(r ** 2 + h ** 2)