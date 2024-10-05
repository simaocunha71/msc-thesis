    def find_coord(lst, x):
        for i, row in enumerate(lst):
            if x in row:
                return i, row.index(x)
        return -1, -1

    result = []
    _, col = find_coord(lst, x)
    result.append((0, col))

    sorted_rows = sorted(lst, key=len)
    for i, row in enumerate(sorted_rows):
        if x in row:
            col = row.index(x)
            result.append((i, col))

    return result


