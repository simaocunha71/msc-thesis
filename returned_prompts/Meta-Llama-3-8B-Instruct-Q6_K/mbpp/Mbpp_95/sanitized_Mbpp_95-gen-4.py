def Find_Min_Length(list_of_lists):
    min_len = float('inf')
    for lst in list_of_lists:
        if len(lst) < min_len:
            min_len = len(lst)
    return min_len