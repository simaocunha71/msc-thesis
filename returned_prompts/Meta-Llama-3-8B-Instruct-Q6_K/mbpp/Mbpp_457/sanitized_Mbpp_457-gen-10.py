def Find_Min(lst):
    min_len = float('inf')
    min_list = []
    for sub in lst:
        if len(sub) < min_len:
            min_len = len(sub)
            min_list = sub
    return min_list