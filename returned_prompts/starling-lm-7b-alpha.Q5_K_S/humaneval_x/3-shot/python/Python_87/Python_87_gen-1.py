    result = []
    for i, row in enumerate(lst):
        if x in row:
            result.append((i, row.index(x)))

    result.sort(key=lambda x: x[0])

    for i, row in enumerate(result):
        result[i] = (row[0], result[i][1])

    result.sort(key=lambda x: x[1], reverse=True)
    return result


