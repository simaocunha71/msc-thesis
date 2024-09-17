def max_length(lst):
    max_len = len(max(lst, key=len))
    max_list = [x for x in lst if len(x) == max_len]
    return max_len, max_list[0]