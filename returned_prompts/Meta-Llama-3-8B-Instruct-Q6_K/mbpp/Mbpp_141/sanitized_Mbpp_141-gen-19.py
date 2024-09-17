def pancake_sort(arr):
    for i in range(len(arr), 0, -1):
        max_index = arr.index(max(arr[:i]))
        if max_index != i - 1:
            if max_index != 0:
                arr[:max_index+1] = arr[:max_index+1][::-1]
            arr[:i] = arr[:i][::-1]
    return arr