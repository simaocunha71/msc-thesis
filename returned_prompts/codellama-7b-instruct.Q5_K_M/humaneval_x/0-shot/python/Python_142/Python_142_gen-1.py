


def sum_squares(lst):
    lst_copy = lst.copy()
    for i, x in enumerate(lst):
        if i % 3 == 0:
            lst_copy[i] = x ** 2
        if i % 4 == 0 and i % 3 != 0:
            lst_copy[i] = x ** 3
    return sum(lst_copy)

