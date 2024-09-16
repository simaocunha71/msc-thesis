def get_coordinates(coordinate_tuple):
    # Your code here
    return [[x + 1, y + 1] for x in range(coordinate_tuple[0] - 1) for y in range(coordinate_tuple[1] - 1)]
