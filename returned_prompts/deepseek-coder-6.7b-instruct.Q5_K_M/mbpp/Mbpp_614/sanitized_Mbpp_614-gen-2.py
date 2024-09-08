def cummulative_sum(tuples):
    total = 0
    for t in tuples:
        total += sum(t)
    return total