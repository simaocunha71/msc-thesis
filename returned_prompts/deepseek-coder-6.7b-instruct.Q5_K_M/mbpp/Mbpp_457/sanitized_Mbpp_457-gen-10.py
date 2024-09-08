def Find_Min(l):
    min_len = min(len(sublist) for sublist in l)
    for sublist in l:
        if len(sublist) == min_len:
            return sublist