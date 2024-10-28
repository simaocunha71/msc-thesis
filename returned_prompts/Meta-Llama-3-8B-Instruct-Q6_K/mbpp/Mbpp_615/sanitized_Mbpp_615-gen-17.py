def average_tuple(tuples):
    result = []
    for t in tuples:
        avg = sum(t) / len(t)
        result.append(avg)
    return result