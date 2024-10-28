    for i in range(len(arr)-1, -1, -1):
        if i == 0 or arr[i] <= arr[i-1]:
            return i
    return -1


