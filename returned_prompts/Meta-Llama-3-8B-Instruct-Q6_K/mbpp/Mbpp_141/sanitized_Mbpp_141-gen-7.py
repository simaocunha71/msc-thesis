def pancake_sort(arr):
    for size in range(len(arr), 0, -1):
        max_idx = arr.index(max(arr[:size]))
        if max_idx != size - 1:
            if max_idx != 0:
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
            arr[:size] = arr[:size][::-1]
    return arr