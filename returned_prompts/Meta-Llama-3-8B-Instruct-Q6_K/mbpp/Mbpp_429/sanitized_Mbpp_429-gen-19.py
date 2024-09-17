def and_tuples(t1, t2):
    result = []
    for x, y in zip(t1, t2):
        if x and y:
            result.append(t1.index(x))
    return tuple(result)