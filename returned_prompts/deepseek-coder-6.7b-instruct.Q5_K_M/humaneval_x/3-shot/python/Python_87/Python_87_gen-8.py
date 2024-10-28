    result = []
    for i, row in enumerate(lst):
        for j, item in enumerate(row):
            if item == x:
                result.append((i, j))
    result.sort()
    result.sort(key=lambda x: x[1], reverse=True)
    return result


