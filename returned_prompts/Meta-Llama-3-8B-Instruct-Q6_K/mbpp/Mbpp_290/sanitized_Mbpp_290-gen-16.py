def max_length(lst):
    max_len = max(len(sublist) for sublist in lst)
    max_sublist = [sublist for sublist in lst if len(sublist) == max_len][0]
    return max_len, max_sublist