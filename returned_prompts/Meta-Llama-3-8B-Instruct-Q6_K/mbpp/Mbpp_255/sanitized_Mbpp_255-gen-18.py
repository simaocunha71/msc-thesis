def combinations_colors(lst, n):
    if n == 0:
        return [()]
    result = []
    for elem in lst:
        for comb in combinations_colors(lst, n-1):
            result.append((elem,) + comb)
    return result