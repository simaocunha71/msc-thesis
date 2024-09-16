"""
def find_kth(arr1, arr2, k):
    total_length = len(arr1) + len(arr2)
    if k > total_length:
        return -1
    if k == total_length:
        return max(arr1[-1], arr2[-1])
    if k <= len(arr1):
        return arr1[k - 1]
    return arr2[k - len(arr1) - 1]
"""
