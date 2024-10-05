    result = []
    for i, row in enumerate(lst):
        for j, elem in enumerate(row):
            if elem == x:
                result.append((i, j))
    return result

