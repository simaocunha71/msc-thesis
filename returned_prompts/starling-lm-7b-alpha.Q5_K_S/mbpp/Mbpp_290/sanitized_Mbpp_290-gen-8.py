def max_length(lists):
    max_len = 0
    max_list = []
    for l in lists:
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return max_len, max_list