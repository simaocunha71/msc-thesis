def surface_Area(base_edge, height):
  slant_height = (base_edge**2 + height**2)**0.5
  base_area = base_edge**2
  lateral_surface_area = 4 * base_edge * slant_height
  total_surface_area = base_area + lateral_surface_area
  return total_surface_area