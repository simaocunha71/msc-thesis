def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return None
    if k <= len(arr1):
        return arr1[k - 1]
    if k <= len(arr1) + len(arr2) // 2:
        return max(arr1[k - 1], arr2[k - len(arr1) - 1])
    return arr2[k - len(arr1) - len(arr2) - 1]