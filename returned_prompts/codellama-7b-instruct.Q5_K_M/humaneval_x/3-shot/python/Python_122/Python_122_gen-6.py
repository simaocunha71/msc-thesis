    if k == 0:
        return 0

    arr = arr[:k]
    arr.sort()

    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return arr[0] + arr[1]

    return arr[0] + arr[1] + arr[2]


