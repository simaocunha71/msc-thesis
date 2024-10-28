def max_aggregate(lst):
    agg_dict = {}
    for name, score in lst:
        if name not in agg_dict or agg_dict[name] < score:
            agg_dict[name] = score
    return max(agg_dict.items(), key=lambda x: x[1])