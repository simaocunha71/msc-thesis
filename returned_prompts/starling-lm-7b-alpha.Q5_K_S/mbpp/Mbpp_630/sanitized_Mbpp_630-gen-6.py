def get_coordinates(coordinate_tuple):
    res = []
    for i in range(coordinate_tuple[0] - 1, coordinate_tuple[0] + 2):
        for j in range(coordinate_tuple[1] - 1, coordinate_tuple[1] + 2):
            res.append([i, j])
    return res