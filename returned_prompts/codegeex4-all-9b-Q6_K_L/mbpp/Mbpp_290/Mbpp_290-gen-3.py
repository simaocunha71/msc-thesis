def max_length(lst):
    max_len = max(len(sublist) for sublist in lst)
    max_len_list = [sublist for sublist in lst if len(sublist) == max_len]
    return max_len, max_len_list
