def get_coordinates(coordinate):
    x, y = coordinate
    adjacent_coordinates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(i, j) for i, j in adjacent_coordinates if 0 <= i < 5 and 0 <= j < 5]