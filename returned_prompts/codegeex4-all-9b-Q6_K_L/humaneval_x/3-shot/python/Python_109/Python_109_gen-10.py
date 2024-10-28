    if len(arr) == 0:
        return True

    sorted_arr = sorted(arr)
    min_val = sorted_arr[0]
    max_val = sorted_arr[-1]

    for i in range(len(arr)):
        if arr[i] == min_val:
            break

    for j in range(i, len(arr)):
        if arr[j] != sorted_arr[j - i]:
            return False

    for k in range(i):
        if arr[k] != sorted_arr[k + len(arr) - i]:
            return False

    return True