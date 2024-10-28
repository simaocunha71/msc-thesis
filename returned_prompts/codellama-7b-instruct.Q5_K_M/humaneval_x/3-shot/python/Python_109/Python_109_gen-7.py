    arr.sort()
    is_sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
    return is_sorted


