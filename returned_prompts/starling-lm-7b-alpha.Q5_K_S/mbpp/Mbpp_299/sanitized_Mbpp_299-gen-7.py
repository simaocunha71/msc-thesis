def max_aggregate(tuples):
    max_agg = (0,0)
    for t in tuples:
        if t[1] > max_agg[1]:
            max_agg = t
    return max_agg