def max_aggregate(lst):
    aggregate = {}
    for name, score in lst:
        if name in aggregate:
            aggregate[name] += score
        else:
            aggregate[name] = score
    return max(aggregate.items(), key=lambda x: x[1])