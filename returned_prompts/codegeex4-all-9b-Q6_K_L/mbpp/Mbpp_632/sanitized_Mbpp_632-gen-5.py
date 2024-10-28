def move_zero(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[count], lst[i] = lst[i], lst[count]
            count += 1
    return lst