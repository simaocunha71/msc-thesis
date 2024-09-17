def surface_Area(base_edge: int, height: int) -> int:
  base_area = base_edge * base_edge
  base_perimeter = 4 * base_edge
  slant_height = math.sqrt((base_edge / 2) ** 2 + height ** 2)
  lateral_area = base_perimeter * slant_height
  return base_area + lateral_area