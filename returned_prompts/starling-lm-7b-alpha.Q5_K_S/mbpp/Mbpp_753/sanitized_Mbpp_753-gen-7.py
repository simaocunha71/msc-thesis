def min_k(tuple_list, k):
    tuple_list.sort(key = lambda x: x[1])
    return tuple_list[:k]