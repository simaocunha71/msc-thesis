from collections import defaultdict
def max_aggregate(people_scores):
    score_dict = defaultdict(int)
    for name, score in people_scores:
        score_dict[name] += score
    return max(score_dict.items(), key=lambda x: x[1]) if score_dict else None