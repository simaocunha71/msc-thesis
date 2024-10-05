    result = l.copy()
    for idx in range(0, len(l), 2):
        result[idx] = sorted(l[idx::2])

    return result


