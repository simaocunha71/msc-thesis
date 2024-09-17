def get_coordinates(coord: tuple) -> list:
    x, y = coord
    adjacent_coords = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
    return adjacent_coords