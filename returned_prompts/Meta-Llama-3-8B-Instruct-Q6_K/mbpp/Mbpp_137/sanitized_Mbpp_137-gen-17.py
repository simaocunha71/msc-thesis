def zero_count(arr):
    zero = 0
    non_zero = 0
    for num in arr:
        if num == 0:
            zero += 1
        else:
            non_zero += 1
    return zero / (zero + non_zero) if zero + non_zero > 0 else 0