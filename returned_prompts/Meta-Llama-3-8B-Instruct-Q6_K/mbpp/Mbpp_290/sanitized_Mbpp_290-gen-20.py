def max_length(list_of_lists):
    max_length = 0
    max_list = []
    for lst in list_of_lists:
        if len(lst) > max_length:
            max_length = len(lst)
            max_list = lst
    return max_length, max_list