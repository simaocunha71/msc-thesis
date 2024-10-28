def get_coordinates(coordinate):
    x, y = coordinate
    return [[x, y] for i in range(y - 1, y + 2) for j in range(x - 1, x + 2)]