def pancake_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i + arr[i:].index(max(arr[i:]))
        if max_idx != i:
            arr[i:max_idx+1] = arr[i:max_idx+1][::-1]
            arr[:max_idx+1] = arr[:max_idx+1][::-1]
    return arr