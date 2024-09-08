def Find_Min_Length(list_of_lists):
    min_length = float('inf')
    for lst in list_of_lists:
        min_length = min(min_length, len(lst))
    return min_length