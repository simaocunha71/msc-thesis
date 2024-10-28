def get_coordinates(coordinate):
  result = []
  x, y = coordinate
  for i in range(-1, 2):
    for j in range(-1, 2):
      result.append([x + i, y + j])
  return result