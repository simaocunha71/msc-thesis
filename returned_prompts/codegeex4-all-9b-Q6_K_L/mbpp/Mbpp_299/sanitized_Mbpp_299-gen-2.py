def max_aggregate(lst):
    from collections import defaultdict
    agg = defaultdict(int)
    for name, score in lst:
        agg[name] += score
    return max(agg.items(), key=lambda x: x[1])