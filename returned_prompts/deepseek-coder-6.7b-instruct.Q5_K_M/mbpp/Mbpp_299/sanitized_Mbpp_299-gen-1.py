def max_aggregate(lst):
    scores = {}
    for name, score in lst:
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score
    max_score = max(scores.values())
    for name, score in scores.items():
        if score == max_score:
            return (name, score)