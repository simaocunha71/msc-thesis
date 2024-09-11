def find_kth(arr1, arr2, k):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if k == 1:
            return min(arr1[i], arr2[j])
        k -= 1
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    while i < len(arr1):
        i += 1
        k -= 1
        if k == 0:
            return arr1[i - 1]
    while j < len(arr2):
        j += 1
        k -= 1
        if k == 0:
            return arr2[j - 1]
    return None