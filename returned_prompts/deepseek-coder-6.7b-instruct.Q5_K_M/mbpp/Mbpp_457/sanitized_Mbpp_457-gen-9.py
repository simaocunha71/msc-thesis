def Find_Min(lst):
    min_len = len(lst[0])
    min_lst = lst[0]
    for sublst in lst:
        if len(sublst) < min_len:
            min_len = len(sublst)
            min_lst = sublst
    return min_lst