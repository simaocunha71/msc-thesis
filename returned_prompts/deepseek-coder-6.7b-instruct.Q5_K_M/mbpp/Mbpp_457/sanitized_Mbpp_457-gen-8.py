def Find_Min(lst):
    min_len = min([len(sublist) for sublist in lst])
    for sublist in lst:
        if len(sublist) == min_len:
            return sublist