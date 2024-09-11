def avg_aggregate(tuples):
    total = 0
    for tup in tuples:
        total += tup[1]
    return (total / len(tuples),)

#