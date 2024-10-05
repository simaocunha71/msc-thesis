def move_one_ball(arr):
    if len(arr) == 0:
        return True

    min_val = min(arr)
    min_idx = arr.index(min_val)

    if min_idx == 0:
        return True

    if min_idx == len(arr) - 1:
        return arr[0] <= arr[1]

    return arr[min_idx] <= arr[min_idx + 1] or arr[min_idx] <= arr[min_idx - 1]

