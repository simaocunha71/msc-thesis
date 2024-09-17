def Find_Min(lst):
    min_len = float('inf')
    min_sublist = []
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
            min_sublist = sublist
    return min_sublist