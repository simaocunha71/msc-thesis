    sum_lst1 = sum([len(i) for i in lst1])
    sum_lst2 = sum([len(i) for i in lst2])
    
    if sum_lst1 < sum_lst2:
        return lst1
    else:
        return lst2


