
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

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))  # ('Juan Whelan', 212)


