    even_indices_values = [l[i] for i in range(0, len(l), 2)]
    even_indices_values.sort()

    result = l.copy()
    for i in range(0, len(result), 2):
        result[i] = even_indices_values.pop(0)

    return result


