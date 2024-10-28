def Find_Min_Length(lst):
    if len(lst) == 0:
        return 0
    else:
        return min(map(len, lst))