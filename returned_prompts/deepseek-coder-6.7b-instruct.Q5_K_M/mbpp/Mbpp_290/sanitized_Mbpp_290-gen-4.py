def max_length(lst):
    max_len = 0
    max_list = []
    for sub_list in lst:
        if len(sub_list) > max_len:
            max_len = len(sub_list)
            max_list = sub_list
    return max_len, max_list