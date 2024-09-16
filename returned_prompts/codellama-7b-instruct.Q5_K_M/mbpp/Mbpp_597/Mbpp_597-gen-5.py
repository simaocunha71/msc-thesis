"""
def find_kth(arr1, arr2, k):
    n = len(arr1)
    m = len(arr2)
    if n > m:
        return find_kth(arr2, arr1, k)
    if n == 0:
        return arr2[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])
    if k > n:
        return find_kth(arr1[1:], arr2, k - n)
    if k < n + 1:
        return find_kth(arr1, arr2[1:], k)
    return find_kth(arr1[1:], arr2[1:], k - n)
"""

