def surface_Area(edge: int,height: int) -> int:
  base_area = edge * edge
  slant_height = math.sqrt((edge / 2) ** 2 + height ** 2)
  slant_area = edge * edge * 2 + edge * slant_height * 4
  return base_area + slant_area


