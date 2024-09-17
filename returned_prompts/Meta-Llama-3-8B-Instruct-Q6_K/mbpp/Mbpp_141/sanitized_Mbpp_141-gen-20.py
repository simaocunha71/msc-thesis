def pancake_sort(arr):
    for size in range(len(arr), 0, -1):
        max_idx = 0
        for i in range(1, size):
            if arr[i] > arr[max_idx]:
                max_idx = i
        if max_idx != size - 1:
            arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
            arr[:size] = arr[:size][::-1]
    return arr