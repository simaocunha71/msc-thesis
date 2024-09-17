def cummulative_sum(tuples):
    total = 0
    for tup in tuples:
        for item in tup:
            total += item
    return total