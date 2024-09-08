def max_aggregate(lst):
    scores = {}
    for name, score in lst:
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score
    max_name = max(scores, key=scores.get)
    return (max_name, scores[max_name])