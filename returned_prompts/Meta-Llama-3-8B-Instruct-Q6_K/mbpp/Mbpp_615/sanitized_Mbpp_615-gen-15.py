def average_tuple(tuples):
    result = []
    for tup in tuples:
        result.append(sum(tup) / len(tup))
    return result