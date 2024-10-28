def Find_Min(lst):
    min_length = float('inf')
    min_sublist = None
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
    return min_sublist