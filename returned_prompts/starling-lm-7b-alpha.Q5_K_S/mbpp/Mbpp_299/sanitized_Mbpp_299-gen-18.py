def max_aggregate(scores):
    return max(scores, key=lambda x: (x[1], x[0]))