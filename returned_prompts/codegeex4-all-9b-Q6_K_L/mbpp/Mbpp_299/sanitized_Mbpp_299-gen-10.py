def max_aggregate(list_of_tuples):
    from collections import defaultdict
    aggregate_dict = defaultdict(int)
    for name, score in list_of_tuples:
        aggregate_dict[name] += score
    return max(aggregate_dict.items(), key=lambda x: x[1])