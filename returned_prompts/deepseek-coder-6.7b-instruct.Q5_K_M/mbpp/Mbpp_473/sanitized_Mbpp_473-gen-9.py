def tuple_intersection(tuples):
    result = set()
    for t in tuples:
        if not result:
            result = set(t)
        else:
            result = result & set(t)
    return result