def find_kth(arr1, arr2, k):
    i = j = k - 1
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            j -= 1
        else:
            i -= 1
    if i >= 0:
        return arr1[i]
    else:
        return arr2[j + 1]  # if arr2[j+1] doesn't exist, return arr2[j]