from collections import defaultdict
def max_aggregate(tups):
    d = defaultdict(int)
    for name, score in tups:
        d[name] += score
    return max(d.items(), key=lambda x: x[1]) # returns the tuple with the maximum score