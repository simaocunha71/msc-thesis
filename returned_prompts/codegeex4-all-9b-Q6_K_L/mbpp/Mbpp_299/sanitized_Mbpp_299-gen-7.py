def max_aggregate(lst):
    from collections import defaultdict
    counts = defaultdict(int)
    for name, score in lst:
        counts[name] += score
    return max(counts.items(), key=lambda x: x[1])