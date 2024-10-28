def get_coordinates(coord):
  x, y = coord
  result = []
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if (i, j) != (x, y):
        result.append([i, j])
  return result
  # or return [[i, j] for i in range(x-1, x+2) for j in range(y-1, y+2) if (i, j) != (x, y)]