def zero_count(arr):
    zero_count = arr.count(0)
    non_zero_count = len(arr) - zero_count
    return zero_count / non_zero_count if non_zero_count else 0