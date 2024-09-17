def pancake_sort(arr):
    result = []
    for size in range(len(arr), 0, -1):
        max_index = arr.index(max(arr[:size]))
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                result.append(max_index + 1)
            arr[:size] = arr[:size][::-1]
            result.append(size - 1)
    return arr