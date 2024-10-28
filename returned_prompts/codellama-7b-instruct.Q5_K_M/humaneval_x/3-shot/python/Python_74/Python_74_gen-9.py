    lst1_total = sum(len(i) for i in lst1)
    lst2_total = sum(len(i) for i in lst2)

    if lst1_total < lst2_total:
        return lst1
    elif lst1_total > lst2_total:
        return lst2
    else:
        return lst1


