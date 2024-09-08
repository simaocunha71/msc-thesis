def max_aggregate(lst):
    from collections import defaultdict
    aggregate = defaultdict(int)
    for name, score in lst:
        aggregate[name] += score
    return max(aggregate.items(), key=lambda x: x[1])