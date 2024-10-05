    result = []
    for i, row in enumerate(lst):
        for j, x in enumerate(row):
            if x == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result


