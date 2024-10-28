def max_aggregate(tuples):
    aggregates = {}
    for name, score in tuples:
        if name in aggregates:
            aggregates[name] += score
        else:
            aggregates[name] = score
    return max(aggregates.items(), key=lambda x: x[1])