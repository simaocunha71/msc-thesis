    coordinates = []

    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                coordinates.append((i, j))

    coordinates.sort(key=lambda x: (x[0], -x[1]))

    return coordinates


