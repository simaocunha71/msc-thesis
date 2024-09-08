def average_tuple(tuples):
    averages = []
    for t in tuples:
        avg = sum(t) / len(t)
        averages.append(avg)
    return averages