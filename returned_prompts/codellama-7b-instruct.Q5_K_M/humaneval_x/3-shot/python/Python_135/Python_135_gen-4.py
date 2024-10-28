    for i, num in enumerate(arr):
        if i > 0 and num <= arr[i-1]:
            return i - 1

    return -1


