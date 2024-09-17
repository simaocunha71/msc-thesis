def len_log(lst):
    max_len = 0
    for word in lst:
        if len(word) > max_len:
            max_len = len(word)
    return max_len