def move_zero(lst):
    non_zero = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[non_zero], lst[i] = lst[i], lst[non_zero]
            non_zero += 1
    return lst