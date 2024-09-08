def last(arr, ele):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == ele:
            return i
    return -1