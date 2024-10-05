    result = []
    for idx, row in enumerate(lst):
        if x in row:
            for col_idx, val in enumerate(reversed(row)):
                if val == x:
                    result.append((idx, len(row) - 1 - col_idx))
                    break
    return result


