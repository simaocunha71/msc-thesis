    for idx, elem in enumerate(arr):
        if arr[idx] > arr[idx-1]:
            return idx - 1
    return -1


