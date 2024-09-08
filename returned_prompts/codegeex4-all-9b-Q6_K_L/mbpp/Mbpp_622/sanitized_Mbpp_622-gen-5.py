def get_median(arr1, arr2, size):
    merged_arr = sorted(arr1 + arr2)
    if size % 2 == 0:
        return (merged_arr[size // 2 - 1] + merged_arr[size // 2]) / 2
    else:
        return merged_arr[size // 2]