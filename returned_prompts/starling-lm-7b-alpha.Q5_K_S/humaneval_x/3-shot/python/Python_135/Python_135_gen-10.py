    for idx, elem in enumerate(arr):
        if idx == 0:
            continue
        if elem > arr[idx-1]:
            return idx-1
    return -1


