def zero_count(arr):
    zero_counter = 0
    non_zero_counter = 0
    for num in arr:
        if num == 0:
            zero_counter += 1
        else:
            non_zero_counter += 1
    return zero_counter/non_zero_counter