def find_kth(arr1, arr2, k):
    if k <= len(arr1) and k > 0:
        return arr1[k - 1]
    elif k <= len(arr2) and k > len(arr1):
        return arr2[k - len(arr1) - 1]
    else:
        return -1