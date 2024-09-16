def get_coordinates(coords):
    adj_coords = []
    for x, y in coords:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            adj_coords.append([x + dx, y + dy])
    return adj_coords
