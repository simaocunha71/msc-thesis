def pancake_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        max_val = max(arr)
        max_index = arr.index(max_val)
        pancake_sort(arr[:max_index])
        pancake_sort(arr[max_index:])
        arr[max_index], arr[0] = arr[0], arr[max_index]
    return arr