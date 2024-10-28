def min_k(tuple_list, k):
    min_tuple_list = sorted(tuple_list, key=lambda x: x[1])
    return min_tuple_list[:k]  # Return the first 'k' elements of the sorted list