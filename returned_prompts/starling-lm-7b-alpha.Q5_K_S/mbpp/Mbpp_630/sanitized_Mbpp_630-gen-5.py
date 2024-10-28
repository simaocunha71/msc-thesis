def get_coordinates(coords):
    left = coords[0] - 1
    right = coords[0] + 1
    up = coords[1] + 1
    down = coords[1] - 1
    return [[left, coords[1]], [right, coords[1]], [coords[0], down], [coords[0], up], [left, down], [left, up], [right, down], [right, up]]