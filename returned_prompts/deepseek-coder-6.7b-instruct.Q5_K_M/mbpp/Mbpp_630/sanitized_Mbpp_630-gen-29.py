def get_coordinates(coordinate):
  x, y = coordinate
  result = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      result.append([x+i, y+j])
  return result