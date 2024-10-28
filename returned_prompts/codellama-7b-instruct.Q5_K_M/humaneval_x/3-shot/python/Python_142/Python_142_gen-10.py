    for idx, number in enumerate(lst):
        if idx % 3 == 0:
            lst[idx] = number ** 2
        elif idx % 4 == 0:
            lst[idx] = number ** 3

    return sum(lst)


