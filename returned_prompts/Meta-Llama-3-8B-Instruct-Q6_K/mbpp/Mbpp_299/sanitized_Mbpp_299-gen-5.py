from collections import defaultdict
def max_aggregate(tup_list):
    aggregate_dict = defaultdict(int)
    for name, score in tup_list:
        aggregate_dict[name] += score
    return max(aggregate_dict.items(), key=lambda x: x[1])