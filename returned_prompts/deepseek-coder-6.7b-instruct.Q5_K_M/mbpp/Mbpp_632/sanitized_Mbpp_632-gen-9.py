def move_zero(lst):
    return [num for num in lst if num != 0] + [0] * lst.count(0)