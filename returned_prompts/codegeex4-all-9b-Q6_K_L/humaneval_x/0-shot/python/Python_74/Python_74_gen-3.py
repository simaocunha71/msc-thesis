def total_match(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return lst1
    elif len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    else:
        count1 = sum(len(s) for s in lst1)
        count2 = sum(len(s) for s in lst2)
        if count1 < count2:
            return lst1
        elif count2 < count1:
            return lst2
        else:
            return lst1