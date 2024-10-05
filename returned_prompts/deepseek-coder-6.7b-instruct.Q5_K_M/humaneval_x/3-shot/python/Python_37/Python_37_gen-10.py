    even_indices = [x for x in range(0, len(l), 2)]
    even_values = sorted([l[i] for i in even_indices])
    result = l.copy()

    for i, v in zip(even_indices, even_values):
        result[i] = v

    return result


