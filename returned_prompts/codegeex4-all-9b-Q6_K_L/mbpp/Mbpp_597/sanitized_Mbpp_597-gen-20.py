def find_kth(arr1: list, arr2: list, k: int):
    len1, len2 = len(arr1), len(arr2)
    if len1 > len2:
        return find_kth(arr2, arr1, k)
    if len1 == 0:
        return arr2[k-1]
    if k == 1:
        return min(arr1[0], arr2[0])
    i = min(len1, k//2)
    j = min(len2, k//2)
    if arr1[i-1] > arr2[j-1]:
        return find_kth(arr1, arr2[j:], k-j)
    else:
        return find_kth(arr1[i:], arr2, k-i)