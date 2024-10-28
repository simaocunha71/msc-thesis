def max_aggregate(lst):
    agg_dict = {}
    for name, score in lst:
        if name in agg_dict:
            agg_dict[name] += score
        else:
            agg_dict[name] = score
    max_name, max_score = max(agg_dict.items(), key=lambda x: x[1])
    return (max_name, max_score)