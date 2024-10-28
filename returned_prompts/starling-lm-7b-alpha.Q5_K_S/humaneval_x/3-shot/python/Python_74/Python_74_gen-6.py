    list1 = 0
    list2 = 0
    for i in lst1:
        list1 += len(i)
    for i in lst2:
        list2 += len(i)
    if list1 < list2:
        return lst2
    elif list1 == list2:
        return lst1
    else:
        return lst1


