def and_tuples(t1, t2):
    result = []
    for i, j in zip(t1, t2):
        if i and j:
            result.append(t1.index(i))
    return tuple(result)