    sum1 = sum(len(i) for i in lst1)
    sum2 = sum(len(i) for i in lst2)
    if sum1 < sum2:
        return lst1
    else:
        return lst2


