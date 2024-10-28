    total_lst1 = 0
    total_lst2 = 0
    for i in lst1:
        total_lst1 += len(i)

    for i in lst2:
        total_lst2 += len(i)

    if total_lst1 < total_lst2:
        return lst1
    elif total_lst1 > total_lst2:
        return lst2
    else:
        return lst1


