def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return -1
    if k <= len(arr1):
        return arr1[k-1]
    if k <= len(arr1) + len(arr2)//2:
        return max(arr1[k-1], find_kth(arr2, arr1, k-len(arr1)))
    return find_kth(arr2, arr1, k-(len(arr1) + len(arr2)//2))