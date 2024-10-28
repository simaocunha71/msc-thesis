def tuple_intersection(tuples):
    result = set()
    for t in tuples:
        for e in t:
            if any(e in t_ for t_ in tuples if t_ != t):
                result.add(t)
    return list(result)