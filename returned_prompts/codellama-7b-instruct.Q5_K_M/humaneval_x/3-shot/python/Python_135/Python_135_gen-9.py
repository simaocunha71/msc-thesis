    for i in range(len(arr)):
        if i > 0 and arr[i] >= arr[i - 1]:
            return i - 1

    return -1


