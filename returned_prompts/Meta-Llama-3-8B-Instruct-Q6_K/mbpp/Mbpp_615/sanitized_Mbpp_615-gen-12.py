def average_tuple(tuples):
    result = []
    for t in tuples:
        result.append(sum(t) / len(t))
    return result