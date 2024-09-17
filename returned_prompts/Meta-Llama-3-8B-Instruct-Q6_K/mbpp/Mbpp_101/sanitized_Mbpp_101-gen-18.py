def kth_element(arr, k):
    k -= 1  # Convert 1-based indexing to 0-based indexing
    if k < 0 or k >= len(arr):
        return None
    return arr[k]