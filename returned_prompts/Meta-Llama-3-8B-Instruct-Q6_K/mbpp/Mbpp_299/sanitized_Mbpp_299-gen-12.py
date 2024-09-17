def max_aggregate(tuples):
    aggregated = {}
    for name, score in tuples:
        if name in aggregated:
            aggregated[name] += score
        else:
            aggregated[name] = score
    return max(aggregated.items(), key=lambda x: x[1])