def find_kth(arr1, arr2, k):
    if len(arr1) + len(arr2) < k:
        return None
    if len(arr1) >= k:
        return arr1[k - 1]
    if len(arr2) >= k - len(arr1):
        return arr2[k - len(arr1) - 1]
    return None
