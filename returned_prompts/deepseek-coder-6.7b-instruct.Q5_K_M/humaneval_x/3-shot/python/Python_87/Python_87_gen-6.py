    coords = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                coords.append((i, j))
    return sorted(coords, key=lambda x: (x[0], -x[1]))


