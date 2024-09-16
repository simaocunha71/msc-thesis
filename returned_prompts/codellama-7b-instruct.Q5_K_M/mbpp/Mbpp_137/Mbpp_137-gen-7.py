def zero_count(arr):
    count_zero = 0
    count_nonzero = 0
    for i in arr:
        if i == 0:
            count_zero += 1
        else:
            count_nonzero += 1
    return count_zero / count_nonzero
