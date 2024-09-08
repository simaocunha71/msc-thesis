def max_aggregate(lst):
    d = {}
    for name, score in lst:
        if name in d:
            d[name] += score
        else:
            d[name] = score
    max_score = max(d.values())
    for name in d:
        if d[name] == max_score:
            return (name, max_score)