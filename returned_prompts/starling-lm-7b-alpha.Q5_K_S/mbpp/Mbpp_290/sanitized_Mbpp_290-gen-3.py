def max_length(l):
    max_len = 0
    max_list = []
    for sublist in l:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return max_len, max_list