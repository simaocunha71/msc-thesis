    lst1_len = sum(len(x) for x in lst1)
    lst2_len = sum(len(x) for x in lst2)
    if lst1_len < lst2_len:
        return lst1
    elif lst1_len > lst2_len:
        return lst2
    else:
        return lst1


