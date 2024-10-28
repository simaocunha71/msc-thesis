def max_length(lst):
    max_len = -1
    max_list = []
    for l in lst:
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return (max_len, max_list)