def remove_kth_element(lst, k):
    return lst[:k-1] + lst[k:]  # slice the list, excluding the kth element