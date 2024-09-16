
def min_k(tuple_list, k):
    # Sort the list based on the second item in each tuple
    sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1])
    # Return the first k items
    return sorted_tuple_list[:k]


