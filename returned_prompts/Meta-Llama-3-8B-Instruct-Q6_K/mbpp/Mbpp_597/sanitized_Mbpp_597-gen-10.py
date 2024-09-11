def find_kth(arr1, arr2, k):
    return sorted([i for i in arr1 + arr2])[k-1] if k > 0 else None