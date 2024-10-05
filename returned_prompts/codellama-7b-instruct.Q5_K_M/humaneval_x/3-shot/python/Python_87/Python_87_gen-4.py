    result = []
    for idx, row in enumerate(lst):
        for idx2, elem in enumerate(row):
            if elem == x:
                result.append((idx, idx2))
    return sorted(result, key=lambda x: x[0])


