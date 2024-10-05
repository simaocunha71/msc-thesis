    result = []
    for row_idx, row in enumerate(lst):
        for col_idx, elem in enumerate(row):
            if elem == x:
                result.append((row_idx, col_idx))

    result.sort()
    result.sort(key=lambda x: x[1], reverse=True)

    return result

