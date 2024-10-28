def max_aggregate(lst):
    from collections import defaultdict
    aggregate_dict = defaultdict(int)
    for name, score in lst:
        aggregate_dict[name] += score
    return max(aggregate_dict.items(), key=lambda x: x[1])