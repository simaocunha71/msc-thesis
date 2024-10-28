
def get_coordinates(coord: tuple) -> list:
  x, y = coord
  coords = []
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      coords.append([i, j])
  return coords


