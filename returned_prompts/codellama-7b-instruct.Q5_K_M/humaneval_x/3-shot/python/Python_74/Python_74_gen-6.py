    if not lst1 and not lst2:
        return lst1
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    lst1_sum = sum([len(x) for x in lst1])
    lst2_sum = sum([len(x) for x in lst2])
    if lst1_sum < lst2_sum:
        return lst1
    elif lst1_sum > lst2_sum:
        return lst2
    else:
        return lst1
