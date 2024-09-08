def tuple_intersection(tuples):
    result = []
    for tup in tuples:
        tup = set(tup)
        if not result:
            result = tup
        else:
            result = result & tup
    return result