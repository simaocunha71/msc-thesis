def find_kth(arr1, arr2, k):
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
        k -= 1
        if k == 0:
            return min(arr1[i], arr2[j])
    if i < len(arr1):
        return arr1[i]
    else:
        return arr2[j]