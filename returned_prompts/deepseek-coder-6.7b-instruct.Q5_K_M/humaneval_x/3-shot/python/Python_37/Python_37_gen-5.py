    even_indices = [v for i, v in enumerate(l) if i % 2 == 0]
    even_indices.sort()

    result = []
    for i, v in enumerate(l):
        if i % 2 == 0:
            result.append(even_indices[i // 2])
        else:
            result.append(v)

    return result


