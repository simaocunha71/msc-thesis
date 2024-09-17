def max_aggregate(lst):
    aggregate = {}
    for name, value in lst:
        aggregate[name] = aggregate.get(name, 0) + value
    max_value = max(aggregate.values())
    max_name = [k for k, v in aggregate.items() if v == max_value]
    return (max_name[0], max_value)