def pancake_sort(arr):
    for size in range(len(arr), 0, -1):
        max_index = 0
        for i in range(1, size):
            if arr[i] > arr[max_index]:
                max_index = i
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
            arr[:size] = arr[:size][::-1]
    return arr