
    if not lst: return []
    rows = []
    for i, row in enumerate(lst):
        for j, el in enumerate(row):
            if el == x:
                rows.append((i, j))
    rows.sort(key=lambda x: x[0])
    return sorted(rows, key=lambda x: x[1], reverse=True)
