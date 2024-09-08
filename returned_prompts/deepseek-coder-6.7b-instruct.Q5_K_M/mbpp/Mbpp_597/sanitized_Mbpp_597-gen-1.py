def find_kth(arr1, arr2, k):
    i = j = 0
    result = None
    while i + j < k:
        if i == len(arr1):
            result = arr2[j]
            j += 1
        elif j == len(arr2):
            result = arr1[i]
            i += 1
        elif arr1[i] < arr2[j]:
            result = arr1[i]
            i += 1
        else:
            result = arr2[j]
            j += 1
    return result