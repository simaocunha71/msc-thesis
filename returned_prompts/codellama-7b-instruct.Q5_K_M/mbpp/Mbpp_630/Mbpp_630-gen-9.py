
def get_coordinates(coord: tuple) -> list:
  x, y = coord
  coord_list = []
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if i != x or j != y:
        coord_list.append([i, j])
  return coord_list


