def Find_Max(lst: list) -> list:
    max_len = max(len(i) for i in lst)
    for i in lst:
        if len(i) == max_len:
            return i