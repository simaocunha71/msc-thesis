    result = []
    for idx, row in enumerate(lst):
        if x in row:
            col_idx = row.index(x)
            result.append((idx, col_idx))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result


