    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            return i
    return -1


