
def max_length(lst_of_lst):
    max_len = 0
    max_len_lst = []
    for lst in lst_of_lst:
        if len(lst) > max_len:
            max_len = len(lst)
            max_len_lst = lst
    return max_len, max_len_lst


