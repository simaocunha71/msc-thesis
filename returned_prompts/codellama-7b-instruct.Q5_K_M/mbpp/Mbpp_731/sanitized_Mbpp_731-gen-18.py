import math
def lateralsurface_cone(r,h):
  lateral_surface = (math.pi * r * (r + (h ** 2) ** 0.5))
  return lateral_surface