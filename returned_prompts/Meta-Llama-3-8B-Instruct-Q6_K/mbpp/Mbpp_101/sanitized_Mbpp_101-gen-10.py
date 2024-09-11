def kth_element(arr, k):
    if k < 1:
        raise ValueError("k should be a positive integer")
    if k > len(arr):
        raise ValueError("k is larger than the array length")
    return arr[k-1]  # subtract 1 for 1-based indexing