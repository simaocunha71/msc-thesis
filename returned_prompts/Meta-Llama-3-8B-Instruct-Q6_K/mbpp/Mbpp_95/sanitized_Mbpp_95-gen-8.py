def Find_Min_Length(list_of_lists):
    return min(len(lst) for lst in list_of_lists) if list_of_lists else None