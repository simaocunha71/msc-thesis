def surface_Area(base_edge, height):
  slant_height = (base_edge**2 + height**2)**0.5
  side_area = 2 * base_edge**2
  base_area = base_edge**2
  slant_area = base_edge * slant_height
  return side_area + base_area + slant_area