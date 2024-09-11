def kth_element(arr, k):
    if k < 1 or k > len(arr):
        return None
    return arr[k-1]  # 1-indexed to 0-indexed