def max_length(lst):
    max_length = 0
    max_list = []
    for sub_list in lst:
        if len(sub_list) > max_length:
            max_length = len(sub_list)
            max_list = sub_list
    return max_length, max_list