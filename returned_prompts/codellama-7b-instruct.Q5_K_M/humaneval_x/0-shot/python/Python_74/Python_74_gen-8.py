
def total_match(lst1, lst2):
    lst1_total = sum(map(len, lst1))
    lst2_total = sum(map(len, lst2))
    if lst1_total < lst2_total:
        return lst1
    elif lst1_total > lst2_total:
        return lst2
    else:
        return lst1