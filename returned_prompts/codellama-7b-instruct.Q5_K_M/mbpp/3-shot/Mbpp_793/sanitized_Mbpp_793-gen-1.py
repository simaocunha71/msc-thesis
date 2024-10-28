def last(arr, x):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == x:
            return i
    return -1