def kth_element(arr, k):
    return sorted(arr)[k-1]  # subtract 1 for 0-based indexing