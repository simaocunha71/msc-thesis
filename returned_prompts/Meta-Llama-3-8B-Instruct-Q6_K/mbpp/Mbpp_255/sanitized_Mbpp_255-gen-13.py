def combinations_colors(lst, n):
    if n == 0:
        return [()]
    result = []
    for element in lst:
        for combination in combinations_colors(lst, n-1):
            result.append((element,) + combination)
    return result