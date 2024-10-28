
def sum_squares(lst):
    lst.sort()
    s = 0
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            s += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            s += lst[i] ** 3
    return s

