    coordinates = []
    for row_index, row in enumerate(lst):
        for col_index, value in enumerate(row):
            if value == x:
                coordinates.append((row_index, col_index))
    return sorted(coordinates, key=lambda tup: (tup[0], -tup[1]))


