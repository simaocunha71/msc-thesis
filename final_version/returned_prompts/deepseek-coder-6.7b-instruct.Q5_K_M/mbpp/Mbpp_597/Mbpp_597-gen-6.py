
def find_kth(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k]
    if len(arr2) == 0:
        return arr1[k]
    if k == 0:
        return min(arr1[0], arr2[0])

    a = arr1[k // 2 - 1] if len(arr1) > k // 2 - 1 else None
    b = arr2[k // 2 - 1] if len(arr2) > k // 2 - 1 else None

    if a is None:
        return find_kth(arr1, arr2[k // 2:], k - k // 2)
    if b is None:
        return find_kth(arr1[k // 2:], arr2, k - k // 2)

    if a < b:
        return find_kth(arr1[k // 2:], arr2, k - k // 2)
    else:
        return find_kth(arr1, arr2[k // 2:], k - k // 2)


assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
This function uses binary search to find the kth element. It takes the median of the two arrays and compares it with k / 2 element. Depending on the result, it either cuts off the first half of the longer array or the second half of the shorter array, and repeats the process on the resulting two arrays.
"""

# 