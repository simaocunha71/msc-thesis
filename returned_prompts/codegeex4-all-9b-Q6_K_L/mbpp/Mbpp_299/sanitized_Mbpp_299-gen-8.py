def max_aggregate(lst):
    result = {}
    for name, score in lst:
        if name not in result:
            result[name] = 0
        result[name] += score
    return max(result.items(), key=lambda x: x[1])