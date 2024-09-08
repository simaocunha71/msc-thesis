def move_zero(lst):
    non_zeroes = [x for x in lst if x != 0]
    zeroes = [x for x in lst if x == 0]
    return non_zeroes + zeroes