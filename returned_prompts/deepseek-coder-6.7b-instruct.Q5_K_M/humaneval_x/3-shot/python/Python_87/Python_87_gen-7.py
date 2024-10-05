    result = []
    for i, row in enumerate(lst):
        for j, item in enumerate(row):
            if item == x:
                result.append((i, j))
    return sorted(result, key=lambda tup: (tup[0], -tup[1]))


