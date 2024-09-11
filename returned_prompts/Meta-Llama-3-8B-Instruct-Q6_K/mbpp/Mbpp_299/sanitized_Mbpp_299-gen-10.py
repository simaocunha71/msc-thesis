from collections import defaultdict
def max_aggregate(tups):
    aggregated = defaultdict(int)
    for name, score in tups:
        aggregated[name] += score
    return max(aggregated.items(), key=lambda x: x[1])  # Return the tuple with the maximum score