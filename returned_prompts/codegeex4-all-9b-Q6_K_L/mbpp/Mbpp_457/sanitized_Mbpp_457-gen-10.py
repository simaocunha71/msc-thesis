def Find_Min(lst):
    min_length = float('inf')
    min_list = []
    for sub_list in lst:
        if len(sub_list) < min_length:
            min_length = len(sub_list)
            min_list = sub_list
    return min_list