def pancake_sort(arr):
    for i in range(len(arr)):
        max_idx = arr.index(max(arr[i:]))
        if max_idx != i:
            arr[:max_idx+1] = arr[:max_idx+1][::-1]
            arr[:i+1] = arr[:i+1][::-1]
    return arr