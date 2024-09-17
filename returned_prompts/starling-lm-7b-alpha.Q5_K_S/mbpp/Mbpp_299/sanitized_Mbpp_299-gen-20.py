def max_aggregate(score_tuple):
    max_scores = {}
    for i in score_tuple:
        if i[0] in max_scores:
            max_scores[i[0]] += i[1]
        else:
            max_scores[i[0]] = i[1]
    max_score = max(max_scores.values())
    for i in max_scores:
        if max_score == max_scores[i]:
            return (i, max_score)