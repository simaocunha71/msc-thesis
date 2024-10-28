
def get_coordinates(coord: tuple) -> list:
  x_coord, y_coord = coord
  x_adjacent_coordinates = [x_coord - 1, x_coord, x_coord + 1]
  y_adjacent_coordinates = [y_coord - 1, y_coord, y_coord + 1]
  adjacent_coordinates = []
  for x, y in zip(x_adjacent_coordinates, y_adjacent_coordinates):
    adjacent_coordinates.append([x, y])
  return adjacent_coordinates


