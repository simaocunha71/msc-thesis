def combinations_colors(lst, length):
    result = []
    for i in range(length):
        result.append(tuple(lst[i] for i in range(length)))
    return result