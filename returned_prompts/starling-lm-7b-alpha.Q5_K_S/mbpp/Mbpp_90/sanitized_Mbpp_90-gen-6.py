def len_log(lst):
    max = 0
    for i in lst:
        if len(i) > max:
            max = len(i)
    return max