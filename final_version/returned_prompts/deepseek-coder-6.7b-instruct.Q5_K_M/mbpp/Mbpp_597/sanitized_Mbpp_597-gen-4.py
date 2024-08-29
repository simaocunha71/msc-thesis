def find_kth(arr1, arr2, k):
    combined = arr1 + arr2
    combined.sort()
    return combined[k - 1]