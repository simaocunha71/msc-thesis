def consecutive_duplicates(lst):
    lst_new = []
    for i in range(len(lst)):
        if i == 0:
            lst_new.append(lst[i])
        else:
            if lst[i] != lst[i-1]:
                lst_new.append(lst[i])
    return lst_new