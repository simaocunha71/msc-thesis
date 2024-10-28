def max_aggregate(lst: list) -> tuple:
    scores = {}
    for name, score in lst:
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score
    return max(scores.items(), key=lambda x: x[1])