def move_zero(lst):
    non_zero = [num for num in lst if num != 0]
    count = len(lst) - len(non_zero)
    return non_zero + [0]*count