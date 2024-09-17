def average_tuple(tuples):
    result = []
    for i, t in enumerate(tuples):
        average = sum(t) / len(t)
        result.append(average)
    return result