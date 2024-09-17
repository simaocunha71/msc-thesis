def max_aggregate(tuples: list) -> list:
    max_aggregate = max(tuples, key = lambda x: x[1])
    return max_aggregate

