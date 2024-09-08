def Find_Max(lst):
    max_len = -1
    max_item = None
    for item in lst:
        if len(item) > max_len:
            max_len = len(item)
            max_item = item
    return max_item