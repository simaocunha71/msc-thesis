
import math
def lateralsurface_cone(r: float, h: float) -> float:
  pi = math.pi
  return pi*r*(h+math.sqrt(h*h + r*r))


