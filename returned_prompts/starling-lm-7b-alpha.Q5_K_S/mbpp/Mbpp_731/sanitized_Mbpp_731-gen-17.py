import math
def lateralsurface_cone(r: float, h: float) -> float:
  return 2*math.pi*r*(r+math.sqrt(h*h+r*r))