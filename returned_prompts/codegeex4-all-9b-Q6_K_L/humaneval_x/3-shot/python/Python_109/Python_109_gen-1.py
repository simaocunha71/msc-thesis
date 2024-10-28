    if len(arr) == 0:
        return True

    sorted_arr = sorted(arr)
    min_idx = arr.index(min(arr))

    return arr == sorted_arr[min_idx:] + arr[:min_idx]