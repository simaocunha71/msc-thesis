def tuple_intersection(t1, t2):
    result = set()
    for t in t1:
        if all(i in any(s) for s in zip(*t2) for i in t):
            result.add(t)
    return tuple(result)