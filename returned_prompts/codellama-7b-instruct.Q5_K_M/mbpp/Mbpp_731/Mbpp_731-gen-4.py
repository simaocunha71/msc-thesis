
import math
def lateral_surface_cone(r: float, h: float) -> float:
  lateral_surface = 2 * math.pi * r * (r + h)
  return lateral_surface


