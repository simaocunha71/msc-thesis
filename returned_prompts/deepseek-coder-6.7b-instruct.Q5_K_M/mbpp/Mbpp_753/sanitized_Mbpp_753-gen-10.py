def min_k(arr, k):
    return sorted(arr, key = lambda x: x[1])[:k]