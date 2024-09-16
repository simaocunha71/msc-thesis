def find_kth(arr1, arr2, k):
    # assuming arr1 and arr2 are sorted
    # assuming k is valid index
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if i + j + 1 == k:
                return arr1[i]
            i += 1
        else:
            if i + j + 1 == k:
                return arr2[j]
            j += 1
    return -1