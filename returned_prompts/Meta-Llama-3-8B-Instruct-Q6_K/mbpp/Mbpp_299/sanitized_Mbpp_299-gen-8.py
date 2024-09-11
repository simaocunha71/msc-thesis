from collections import defaultdict
def max_aggregate(tuples):
    aggregated = defaultdict(int)
    for name, score in tuples:
        aggregated[name] += score
    return max(aggregated.items(), key=lambda x: x[1])  # Return the tuple with the maximum aggregated score