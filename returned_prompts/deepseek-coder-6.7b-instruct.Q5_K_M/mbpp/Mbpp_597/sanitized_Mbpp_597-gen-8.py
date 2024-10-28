def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return -1
    if len(arr1) == 0:
        return arr2[k - 1]
    if len(arr2) == 0:
        return arr1[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])

    mid1 = min(len(arr1), k // 2)
    mid2 = min(len(arr2), k // 2)

    if arr1[mid1 - 1] > arr2[mid2 - 1]:
        return find_kth(arr1, arr2[mid2:], k - mid2)
    else:
        return find_kth(arr1[mid1:], arr2, k - mid1)