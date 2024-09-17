def find_kth(arr1, arr2, k):
    if not arr1:
        return arr2[k - 1]
    if not arr2:
        return arr1[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])
    i, j = (k // 2) - 1, (k // 2) - 1
    if arr1[i + 1] < arr2[j + 1]:
        return find_kth(arr1[i + 1:], arr2, k - i - 1)
    elif arr2[j + 1] < arr1[i + 1]:
        return find_kth(arr1, arr2[j + 1:], k - j - 1)
    else:
        return arr1[i + 1]