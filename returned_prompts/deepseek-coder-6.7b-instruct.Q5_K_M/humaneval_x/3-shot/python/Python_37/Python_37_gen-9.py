    even_indicies = [i for i, e in enumerate(l) if i % 2 == 0]
    sorted_even_values = sorted([l[i] for i in even_indicies])

    result = l.copy()
    for i, e in enumerate(even_indicies):
        result[e] = sorted_even_values[i]

    return result


