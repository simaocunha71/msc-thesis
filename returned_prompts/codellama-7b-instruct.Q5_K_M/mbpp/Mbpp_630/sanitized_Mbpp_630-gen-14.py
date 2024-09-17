def get_coordinates(coords):
  x, y = coords
  return [
    [x-1, y-1], [x-1, y], [x-1, y+1],
    [x, y-1], [x, y], [x, y+1],
    [x+1, y-1], [x+1, y], [x+1, y+1]
  ]