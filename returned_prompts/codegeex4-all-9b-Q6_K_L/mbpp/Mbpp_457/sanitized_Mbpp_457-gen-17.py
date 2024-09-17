def Find_Min(lists):
    min_length = min(len(l) for l in lists)
    for l in lists:
        if len(l) == min_length:
            return l