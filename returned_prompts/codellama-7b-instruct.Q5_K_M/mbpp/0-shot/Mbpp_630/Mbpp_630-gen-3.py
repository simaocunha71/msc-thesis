def get_coordinates(coordinates):
    x, y = coordinates
    return [[x + i, y + j] for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
