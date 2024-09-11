from collections import defaultdict
def max_aggregate(tuples):
    name_to_sum = defaultdict(int)
    for name, score in tuples:
        name_to_sum[name] += score
    return max(name_to_sum.items(), key=lambda x: x[1])  # Return the tuple with the maximum sum