def Find_Min(list_of_lists):
    min_length = min(len(lst) for lst in list_of_lists)
    return [lst for lst in list_of_lists if len(lst) == min_length][0]  # returns the first sublist with minimum length