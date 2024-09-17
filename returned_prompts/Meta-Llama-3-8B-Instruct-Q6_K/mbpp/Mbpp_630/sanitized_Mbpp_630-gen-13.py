def get_coordinates(coord, max_x, max_y):
    x, y = coord
    return [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
    adjacent_coords = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y:
                adjacent_coords.append([x + dx, y + dy])
    return adjacent_coords