import math
def lateralsurface_cone(r: float, h: float) -> float:
  pi = math.pi
  return pi * r * (2 + math.sqrt(1 + (h / r)**2))