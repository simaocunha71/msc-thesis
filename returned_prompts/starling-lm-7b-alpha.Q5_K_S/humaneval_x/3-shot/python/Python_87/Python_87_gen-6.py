    result = []
    for i, r in enumerate(lst):
        for j, elem in enumerate(r):
            if elem == x:
                result.append((i, j))

    result.sort(key=lambda x: (x[0], -x[1]))
    return result


