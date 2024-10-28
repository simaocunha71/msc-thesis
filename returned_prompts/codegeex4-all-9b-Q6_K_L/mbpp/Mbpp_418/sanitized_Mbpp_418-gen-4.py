def Find_Max(lst):
    max_len = max(len(x) for x in lst)
    for item in lst:
        if len(item) == max_len:
            return item