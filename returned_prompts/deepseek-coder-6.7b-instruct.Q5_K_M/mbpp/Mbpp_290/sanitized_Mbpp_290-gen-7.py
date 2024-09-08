def max_length(lst):
    max_len = -1
    max_lst = []
    for sub_lst in lst:
        if len(sub_lst) > max_len:
            max_len = len(sub_lst)
            max_lst = sub_lst
    return (max_len, max_lst)