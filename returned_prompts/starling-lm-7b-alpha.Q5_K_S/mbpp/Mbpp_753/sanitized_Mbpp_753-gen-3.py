def min_k(tup_list, k):
    tup_list = sorted(tup_list, key=lambda x: x[1])
    return tup_list[:k]