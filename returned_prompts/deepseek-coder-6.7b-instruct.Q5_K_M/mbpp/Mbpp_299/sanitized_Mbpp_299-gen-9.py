def max_aggregate(lst):
    scores = {}
    for name, score in lst:
        if name not in scores:
            scores[name] = 0
        scores[name] += score
    max_score = max(scores.values())
    max_name = [k for k, v in scores.items() if v == max_score]
    return (max_name[0], max_score)