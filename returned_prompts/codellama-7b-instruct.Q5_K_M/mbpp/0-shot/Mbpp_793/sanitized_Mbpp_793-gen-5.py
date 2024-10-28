def last(arr, ele):
    # your code goes here
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == ele:
            return i
    return -1