def min_k(tup_list, k):
    return sorted(tup_list, key=lambda x: x[1])[:k]