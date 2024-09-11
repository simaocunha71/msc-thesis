def min_k(records, k):
    return sorted(records, key=lambda x: x[1])[:k]  # sort by the second element of the tuple and return the first k elements