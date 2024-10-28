    result = []
    for i, row in enumerate(lst):
        for j, elem in enumerate(row):
            if elem == x:
                result.append((i, j))

    return sorted(result, key=lambda x: (x[0], -x[1]))