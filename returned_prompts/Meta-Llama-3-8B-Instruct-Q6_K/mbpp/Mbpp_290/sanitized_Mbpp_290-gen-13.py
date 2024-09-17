def max_length(list_of_lists):
    if not list_of_lists:
        return None
    max_len = 0
    max_list = None
    for l in list_of_lists:
        if not l:
            return None
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return max_len, max