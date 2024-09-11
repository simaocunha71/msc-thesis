def pancake_sort(arr):
    for i in range(len(arr)):
        max_index = arr.index(max(arr[:i+1]))
        if max_index != i:
            arr[:max_index+1] = reversed(arr[:max_index+1])
            arr[:i+1] = reversed(arr[:i+1])
    return arr