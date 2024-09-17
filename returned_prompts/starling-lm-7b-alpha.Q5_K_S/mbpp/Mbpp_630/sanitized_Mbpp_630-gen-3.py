def get_coordinates(coordinate):
    x, y = coordinate
    result = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            result.append([i, j])
    return result