
def find_kth(arr1, arr2, k):
    if k <= 0:
        raise ValueError("k should be positive")
    if len(arr1) + len(arr2) < k:
        raise ValueError("k is out of range")
    i = 0
    j = 0
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
    if i < len(arr1):
        while i < len(arr1) and k > 0:
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
    else:
        while j < len(arr2) and k > 0:
            k -= 1
            if k == 0:
                return arr2[j]
            j += 1
    raise ValueError("No kth element found")


