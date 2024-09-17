def len_log(list1):
    max_len = 0
    for i in list1:
        if len(i) > max_len:
            max_len = len(i)
    return max_len