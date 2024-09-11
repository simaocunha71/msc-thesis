def kth_element(arr, k):
    return arr[k-1] if k > 0 and k <= len(arr) else None