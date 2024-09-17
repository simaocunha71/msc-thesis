def surface_Area(base_edge, height):
  base_area = base_edge * base_edge
  slant_height = math.sqrt((base_edge/2)**2 + height**2)
  slant_area = base_edge * slant_height
  total_area = base_area + 2 * slant_area
  return total_area