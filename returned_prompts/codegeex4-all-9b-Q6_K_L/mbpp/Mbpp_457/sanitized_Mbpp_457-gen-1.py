def Find_Min(lst):
    min_length = min(map(len, lst))
    for sublist in lst:
        if len(sublist) == min_length:
            return sublist