def tuple_intersection(tuples):
    result = set()
    for tup in tuples:
        if not result:  # first tuple
            result = set(tup)
        else:
            result = result & set(tup)  # find intersection
    return result