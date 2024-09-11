def min_k(tuple_list, k):
    return sorted(tuple_list, key=lambda x: x[1])[:k]  # sort by the second element of each tuple and return the first k elements