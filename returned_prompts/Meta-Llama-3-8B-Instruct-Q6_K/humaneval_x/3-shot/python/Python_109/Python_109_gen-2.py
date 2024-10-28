    if not arr:
        return True

    n = len(arr)
    max_idx = 0

    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i

    for i in range(n - 1, -1, -1):
        if i != max_idx and arr[i] < arr[max_idx]:
            return False

    return True


