def get_coordinates(coord):
    x, y = coord
    adjacent_coordinates = [[x-1, y-1], [x-1, y], [x-1, y+1],
                            [x, y-1],            [x, y+1],
                            [x+1, y-1], [x+1, y], [x+1, y+1]]
    return adjacent_coordinates