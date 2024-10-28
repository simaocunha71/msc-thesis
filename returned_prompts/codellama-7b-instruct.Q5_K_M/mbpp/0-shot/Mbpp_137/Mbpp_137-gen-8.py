def zero_count(arr):
    zeroes = 0
    non_zeroes = 0
    for num in arr:
        if num == 0:
            zeroes += 1
        else:
            non_zeroes += 1
    return zeroes / non_zeroes
