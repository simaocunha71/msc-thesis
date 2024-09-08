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