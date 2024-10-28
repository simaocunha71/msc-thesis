    result = []
    for row_idx, row in enumerate(lst):
        for col_idx, col in enumerate(row):
            if col == x:
                result.append((row_idx, col_idx))
    return sorted(result, key=lambda x: (x[0], -x[1]))
