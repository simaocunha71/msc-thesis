    # list of coordinates of the row
    coordinates = []
    # list of coordinates of the row, sorted by columns in descending order
    coordinates_sorted = []
    # current row
    current_row = 0

    for row in lst:
        # current column
        current_column = 0
        # current coordinate
        current_coords = (current_row, current_column)
        # if the row contains x, add the coordinate
        if x in row:
            coordinates.append(current_coords)
        # if the row does not contain x, move to next row
        else:
            current_row += 1

    # sort coordinates by rows in ascending order
    coordinates = sorted(coordinates, key=lambda x: x[0])

    # sort coordinates of each row by columns in descending order
    for coordinates_row in coordinates:
        coordinates_sorted.extend(sorted(coordinates_row, key=lambda x: x[1], reverse=True))

    return coordinates_sorted


