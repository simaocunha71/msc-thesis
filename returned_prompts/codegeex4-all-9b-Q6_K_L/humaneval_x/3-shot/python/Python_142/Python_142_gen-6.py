    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 == 0:
            lst[i] = lst[i] ** 3
        elif i % 3 == 0:
            lst[i] = lst[i] ** 2
    return sum(lst)

