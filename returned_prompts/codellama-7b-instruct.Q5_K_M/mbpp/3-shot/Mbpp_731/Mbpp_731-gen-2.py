
import math
def lateralsurface_cone(r: float, h: float) -> float:
  lateral_surface = (math.pi * r * (r + (h/2)))
  return lateral_surface


