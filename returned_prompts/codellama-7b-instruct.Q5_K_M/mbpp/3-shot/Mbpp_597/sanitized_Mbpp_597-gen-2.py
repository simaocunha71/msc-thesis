def find_kth(arr1, arr2, k):
    return arr1[k-1] if k <= len(arr1) else arr2[k-len(arr1)-1]