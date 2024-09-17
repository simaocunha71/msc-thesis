def Find_Min(sublists):
    min_length = len(sublists[0])
    min_sublist = sublists[0]
    for sublist in sublists:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
    return min_sublist