def find_kth(arr1, arr2, k):
    i = j = 0
    for _ in range(k):
        if i == len(arr1):
            return arr2[j]
        if j == len(arr2):
            return arr1[i]
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return arr1[i] if i < j else arr2[j]  # Return the kth element