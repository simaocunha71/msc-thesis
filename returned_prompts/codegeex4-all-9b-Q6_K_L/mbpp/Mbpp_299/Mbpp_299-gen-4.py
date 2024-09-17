def max_aggregate(list_of_tuples: list) -> tuple:
    max_aggregate = max(list_of_tuples, key=lambda x: x[1])
    return max_aggregate

