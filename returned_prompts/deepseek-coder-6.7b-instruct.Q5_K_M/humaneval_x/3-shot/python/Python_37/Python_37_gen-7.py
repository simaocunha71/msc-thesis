    even_indicies_values = [l[i] for i in range(0, len(l), 2)]
    even_indicies_values.sort()

    result = l[:]
    for i in range(0, len(result), 2):
        result[i] = even_indicies_values[i // 2]

    return result


