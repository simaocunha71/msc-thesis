def max_length(lst):
    max_len = max(len(i) for i in lst)
    max_len_list = [i for i in lst if len(i) == max_len]
    return max_len, max_len_list

