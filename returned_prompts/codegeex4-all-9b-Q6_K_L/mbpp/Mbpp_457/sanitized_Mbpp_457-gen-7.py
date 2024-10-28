def Find_Min(lst):
    min_len = float('inf')
    min_lst = None
    for sub_lst in lst:
        if len(sub_lst) < min_len:
            min_len = len(sub_lst)
            min_lst = sub_lst
    return min_lst