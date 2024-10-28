def zero_count(arr):
    zero = arr.count(0)
    non_zero = len(arr) - zero
    return zero / non_zero