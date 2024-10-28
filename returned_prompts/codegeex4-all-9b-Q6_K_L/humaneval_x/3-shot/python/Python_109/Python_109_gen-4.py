    if len(arr) == 0:
        return True

    sorted_arr = sorted(arr)
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))

    if min_idx <= max_idx:
        return arr[max_idx:] + arr[:max_idx] == sorted_arr
    else:
        return arr[max_idx:] + arr[:max_idx] == sorted_arr or arr[max_idx:] + arr[:max_idx] == sorted_arr[::-1]

