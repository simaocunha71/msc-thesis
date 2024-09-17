def zero_count(arr):
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
    non_zero_count = len(arr) - zero_count
    return zero_count / non_zero_count if non_zero_count > 0 else 0