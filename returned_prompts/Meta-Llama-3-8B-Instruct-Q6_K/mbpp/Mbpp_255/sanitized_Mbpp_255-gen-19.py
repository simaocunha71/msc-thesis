def combinations_colors(lst, n):
    if n == 0:
        return [()]
    result = []
    for i in range(len(lst)):
        for combination in combinations_colors(lst[i+1:], n-1):
            result.append((lst[i],) + combination)
    return result