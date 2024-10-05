    result = []
    for i, row in enumerate(lst):
        if x in row:
            for j, val in enumerate(reversed(row)):
                if val == x:
                    result.append((i, j))
    return result


