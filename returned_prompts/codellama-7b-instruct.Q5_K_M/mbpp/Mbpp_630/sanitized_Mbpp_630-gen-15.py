def get_coordinates(coordinate_tuple: tuple) -> list:
  x, y = coordinate_tuple
  coordinates = []
  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      if (i, j) != coordinate_tuple:
        coordinates.append([i, j])
  return coordinates