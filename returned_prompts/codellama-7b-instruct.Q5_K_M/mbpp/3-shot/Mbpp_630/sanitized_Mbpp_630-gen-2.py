def get_coordinates(coord_tuple):
  x, y = coord_tuple
  return [[x + 1, y + 1], [x + 1, y], [x + 1, y - 1], [x, y + 1], [x, y], [x, y - 1], [x - 1, y + 1], [x - 1, y], [x - 1, y - 1]]