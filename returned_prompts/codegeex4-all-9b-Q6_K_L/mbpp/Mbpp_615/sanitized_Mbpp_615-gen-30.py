def average_tuple(tuples: tuple) -> list:
    averages = [sum(t)/len(t) for t in tuples]
    return averages