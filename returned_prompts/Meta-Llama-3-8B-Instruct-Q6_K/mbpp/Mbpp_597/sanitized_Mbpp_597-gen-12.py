def find_kth(arr1, arr2, k):
    if k == 1:
        return min(arr1[0], arr2[0])
    idx1, idx2 = 0, 0
    while k > 1:
        if idx1 + 1 >= len(arr1):
            return arr2[k - 1]
        if idx2 + 1 >= len(arr2):
            return arr1[k - 1]
        if arr1[idx1] < arr2[idx2]:
            k -= 1
            idx1 += 1
        else:
            k -= 1
            idx2 += 1
    if k == 1:
        if arr1[idx1] < arr2[idx2]:
            return arr1[idx1]
        else:
            return arr2[idx2]
    if idx1 + 1 >= len(arr1):
        return arr2[idx2]
    if idx2 + 1 >= len(arr2):
        return arr1[idx1]
    if arr1[idx1] < arr2[idx2]:
        return arr1[idx1 + 1]
    else:
        return arr2[idx2 + 1]