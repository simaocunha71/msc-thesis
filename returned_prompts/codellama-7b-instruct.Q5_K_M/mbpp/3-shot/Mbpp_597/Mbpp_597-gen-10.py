
def find_kth(arr1: list, arr2: list, k: int) -> int:
    if len(arr1) < k:
        return arr2[k - len(arr1) - 1]
    if len(arr2) < k:
        return arr1[k - len(arr2) - 1]
    if arr1[k - 1] > arr2[k - 1]:
        return find_kth(arr1[:k - 1], arr2, k - 1)
    else:
        return find_kth(arr1, arr2[:k - 1], k - 1)


