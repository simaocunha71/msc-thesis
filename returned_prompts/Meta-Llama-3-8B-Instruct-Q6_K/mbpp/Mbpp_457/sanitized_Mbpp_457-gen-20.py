def Find_Min(lst):
    min_len = float('inf')
    min_lst = []
    for sub in lst:
        if len(sub) < min_len:
            min_len = len(sub)
            min_lst = sub
    return min_lst