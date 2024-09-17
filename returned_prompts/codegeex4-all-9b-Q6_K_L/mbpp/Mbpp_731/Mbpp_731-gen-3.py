import math
def lateralsurface_cone(r: float, h: float) -> float:
  lateral_surface_area = math.pi * r * math.sqrt(r**2 + h**2)
  return lateral_surface_area

