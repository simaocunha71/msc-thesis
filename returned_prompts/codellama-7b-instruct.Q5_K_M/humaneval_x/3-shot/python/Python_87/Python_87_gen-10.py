    result = []

    for y, row in enumerate(lst):
        for x, col in enumerate(row):
            if col == x:
                result.append((y, x))

    return sorted(result, key=lambda x: (x[0], -x[1]))


