def average_tuple(tuples):
    averages = []
    for tup in tuples:
        averages.append(sum(tup)/len(tup))
    return averages