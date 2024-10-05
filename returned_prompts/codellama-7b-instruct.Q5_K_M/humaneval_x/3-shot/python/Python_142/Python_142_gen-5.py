    lst2 = lst.copy()
    for i in range(len(lst2)):
        if i % 4 == 0:
            lst2[i] = lst2[i] ** 3
        elif i % 3 == 0:
            lst2[i] = lst2[i] ** 2
    return sum(lst2)


