def combinations_colors(lst, n):
    if n == 0:
        return [()]
    else:
        result = []
        for x in lst:
            for p in combinations_colors(lst, n-1):
                result.append((x,) + p)
        return result