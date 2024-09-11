def average_tuple(tuple_of_tuples):
    average = []
    for t in tuple_of_tuples:
        average.append(sum(t) / len(t))
    return average