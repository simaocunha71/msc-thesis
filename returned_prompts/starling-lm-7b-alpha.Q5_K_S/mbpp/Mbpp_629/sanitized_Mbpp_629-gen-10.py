def Split(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst