def find_kth(arr1, arr2, k):
    if k <= 0:
        return None
    if len(arr1) == 0:
        return arr2[k-1]
    if len(arr2) == 0:
        return arr1[k-1]
    if k == 1:
        return min(arr1[0], arr2[0])
    i = min(k//2, len(arr1))
    j = min(k//2, len(arr2))
    if arr1[i-1] < arr2[j-1]:
        return find_kth(arr1[i:], arr2, k-i)
    elif arr1[i-1] > arr2[j-1]:
        return find_kth(arr1, arr2[j:], k-j)
    else:
        return arr1[i-1]