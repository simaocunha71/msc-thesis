def max_aggregate(tuples):
    return max(tuples, key=lambda x: sum(x[1:]))