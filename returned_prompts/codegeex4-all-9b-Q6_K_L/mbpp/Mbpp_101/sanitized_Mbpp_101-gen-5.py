def kth_element(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("Invalid value of k")
    return sorted(arr)[k-1]