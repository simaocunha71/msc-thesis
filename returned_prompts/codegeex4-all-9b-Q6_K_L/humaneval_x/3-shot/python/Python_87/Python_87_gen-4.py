    result = []
    for idx, row in enumerate(lst):
        for idx2, elem in enumerate(row):
            if elem == x:
                result.append((idx, idx2))

    result.sort(key=lambda x: x[0])
    for row in result:
        row[1] = len(lst[row[0]]) - row[1] - 1

    return result

