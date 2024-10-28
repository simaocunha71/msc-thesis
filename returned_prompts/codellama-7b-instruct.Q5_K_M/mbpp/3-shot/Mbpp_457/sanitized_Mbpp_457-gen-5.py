def Find_Min(my_list):
    min_len = len(my_list[0])
    min_sublist = my_list[0]
    for sublist in my_list[1:]:
        if len(sublist) < min_len:
            min_len = len(sublist)
            min_sublist = sublist
    return min_sublist