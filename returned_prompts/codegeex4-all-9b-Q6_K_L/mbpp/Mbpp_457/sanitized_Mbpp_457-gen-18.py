def Find_Min(lst):
    min_length = min(len(i) for i in lst)
    for i in lst:
        if len(i) == min_length:
            return i