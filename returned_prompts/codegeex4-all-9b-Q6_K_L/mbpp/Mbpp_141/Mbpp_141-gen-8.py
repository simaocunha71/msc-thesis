def pancake_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        max_index = arr.index(max(arr[:i+1]))
        if max_index != i:
            arr[:max_index+1] = sorted(arr[:max_index+1], reverse=True)
            arr[:i+1] = sorted(arr[:i+1], reverse=True)
    return arr

