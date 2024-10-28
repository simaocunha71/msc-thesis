


def sum_squares(lst):
    for index, value in enumerate(lst):
        if index % 3 == 0:
            lst[index] = lst[index] ** 2
        elif index % 4 == 0 and index % 3 != 0:
            lst[index] = lst[index] ** 3
    return sum(lst)
