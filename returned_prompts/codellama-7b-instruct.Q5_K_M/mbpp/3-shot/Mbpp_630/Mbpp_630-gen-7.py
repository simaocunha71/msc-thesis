
def get_coordinates(coord):
  x, y = coord
  adjacent_coords = []
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      adjacent_coords.append([i, j])
  return adjacent_coords


