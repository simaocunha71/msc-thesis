    total_lst = []
    for i in range(len(lst1)):
        if len(lst1[i]) < len(lst2[i]):
            total_lst.append(lst1[i])
        else:
            total_lst.append(lst2[i])

    if len(total_lst) > 0:
        return total_lst
    else:
        return lst1