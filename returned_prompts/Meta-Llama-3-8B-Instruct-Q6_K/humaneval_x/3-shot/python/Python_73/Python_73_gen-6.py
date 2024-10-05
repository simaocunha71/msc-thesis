    n = len(arr)
    # create a mirror image of the array
    arr_mirror = arr[::-1]
    # count the number of differences between the original array and the mirrored array
    diff_count = sum(1 for i in range(n) if arr[i] != arr_mirror[i])
    return diff_count
