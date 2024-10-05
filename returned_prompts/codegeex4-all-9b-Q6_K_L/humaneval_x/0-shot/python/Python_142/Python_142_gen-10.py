def sum_squares(lst):
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            lst[i] **= 2
        elif i % 4 == 0:
            lst[i] **= 3
    return sum(lst)