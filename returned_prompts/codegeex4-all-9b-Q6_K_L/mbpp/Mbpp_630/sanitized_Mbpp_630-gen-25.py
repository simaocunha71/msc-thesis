def get_coordinates(coord: tuple):
    x, y = coord
    return [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]