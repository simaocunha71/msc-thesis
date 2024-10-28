from math import pi
def lateralsurface_cone(r, h):
  lateral_surface_area = 2 * pi * r * (r + (h ** 2) ** 0.5)
  return lateral_surface_area