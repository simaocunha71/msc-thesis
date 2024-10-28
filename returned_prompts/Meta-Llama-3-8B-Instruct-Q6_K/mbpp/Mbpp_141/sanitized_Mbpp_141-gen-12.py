def pancake_sort(arr):
    for i in range(len(arr), 0, -1):
        max_idx = arr.index(max(arr[:i]))
        if max_idx != i - 1:
            if max_idx != 0:
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
            arr[:i] = arr[:i][::-1]
    return arr