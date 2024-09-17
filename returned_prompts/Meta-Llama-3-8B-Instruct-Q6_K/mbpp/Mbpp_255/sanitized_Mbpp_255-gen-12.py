def combinations_colors(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(n):
            result.append((lst[i],))
    return result