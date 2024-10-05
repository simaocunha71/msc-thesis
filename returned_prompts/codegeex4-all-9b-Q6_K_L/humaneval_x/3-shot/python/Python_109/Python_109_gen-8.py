    if len(arr) == 0:
        return True

    sorted_arr = sorted(arr)
    min_value = sorted_arr[0]

    for i in range(len(arr)):
        if arr[i] == min_value:
            break

    return arr[i:] + arr[:i] == sorted_arr