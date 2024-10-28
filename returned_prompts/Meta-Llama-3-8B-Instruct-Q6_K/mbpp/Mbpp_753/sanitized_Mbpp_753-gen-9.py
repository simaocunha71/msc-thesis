def min_k(records, k):
    return sorted(records, key=lambda x: x[1])[:k]
    # or
    return sorted(records, key=lambda x: x[1])[-k:]  # if you want the k smallest records