def and_tuples(t1, t2):
    result = []
    for x, y in zip(t1, t2):
        if x & y:
            result.append(t1.index(x))
        else:
            result.append(t1.index(y))
    return tuple(result) if result else None