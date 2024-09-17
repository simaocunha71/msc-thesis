
def find_kth(arr1, arr2, k):
    if k == 1:
        return min(arr1[0], arr2[0])
    if k == len(arr1) + len(arr2):
        return max(arr1[-1], arr2[-1])

    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
            j += 1

    if i == len(arr1):
        while j < len(arr2):
            k -= 1
            if k == 0:
                return arr2[j]
            j += 1
    else:
        while i < len(arr1):
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
    return -1


