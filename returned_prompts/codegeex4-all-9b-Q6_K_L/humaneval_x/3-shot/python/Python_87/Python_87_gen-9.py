    result = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                result.append((i, j))
    return result

