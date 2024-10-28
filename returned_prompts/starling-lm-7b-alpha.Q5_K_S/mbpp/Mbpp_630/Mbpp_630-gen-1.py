
def get_coordinates(coord):
    x, y = coord
    return [[x, y], [x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1], [x - 1, y - 1], [x + 1, y - 1], [x - 1, y + 1], [x + 1, y + 1]]


