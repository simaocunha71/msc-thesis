def get_coordinates(point):
  x, y = point
  coords = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
  return [(x, y) for x, y in coords if 0 <= x <= 5 and 0 <= y <= 5]