    result = []
    n_levels = n
    while n_levels > 0:
        result.append(n_levels)
        if n_levels % 2 == 0:
            n_levels += 2
        else:
            n_levels += 1
    return result


