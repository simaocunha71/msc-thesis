    even_indices = [x for i, x in enumerate(l) if i % 2 == 0]
    even_indices.sort()
    result = []
    idx = 0

    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even_indices[idx])
            idx += 1
        else:
            result.append(x)

    return result

