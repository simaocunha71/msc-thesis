def kth_element(arr, k):
    if k > len(arr):
        return None
    return arr[k-1] # since 1-based indexing, subtract 1 from k