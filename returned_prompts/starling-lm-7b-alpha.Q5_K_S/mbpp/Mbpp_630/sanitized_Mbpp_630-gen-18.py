def get_coordinates(coordinate: tuple) -> list:
  x,y = coordinate
  return [[x,y-1], [x,y], [x,y+1], [x+1,y], [x,y], [x-1,y], [x+1,y-1], [x+1,y+1], [x-1,y+1]]