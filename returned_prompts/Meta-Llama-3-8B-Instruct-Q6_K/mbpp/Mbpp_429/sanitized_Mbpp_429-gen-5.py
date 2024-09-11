def and_tuples(t1, t2):
    result = []
    for i, j in zip(t1, t2):
        if i & j:
            result.append(t1.index(i))
        else:
            result.append(0)
    return tuple(result)