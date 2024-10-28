def max_length(lst):
    max_length = 0
    max_list = []
    for sublist in lst:
        if len(sublist) > max_length:
            max_length = len(sublist)
            max_list = sublist
    return max_length, max_list


