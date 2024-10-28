def pancake_sort(arr):
    for i in range(len(arr) - 1):
        max_index = arr.index(max(arr[i+1:]))
        if max_index != i:
            if max_index != i:
                arr[:max_index+1] = arr[:max_index+1][::-1]
            arr[:i+1] = arr[:i+1][::-1]
    return arr