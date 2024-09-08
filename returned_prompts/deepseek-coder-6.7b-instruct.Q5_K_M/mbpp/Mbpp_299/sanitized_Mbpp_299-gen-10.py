def max_aggregate(lst):
    name_score_dict = {}
    for name, score in lst:
        if name in name_score_dict:
            name_score_dict[name] += score
        else:
            name_score_dict[name] = score
    max_score = max(name_score_dict.values())
    max_aggregate_name = [k for k, v in name_score_dict.items() if v == max_score]
    return (max_aggregate_name[0], max_score)