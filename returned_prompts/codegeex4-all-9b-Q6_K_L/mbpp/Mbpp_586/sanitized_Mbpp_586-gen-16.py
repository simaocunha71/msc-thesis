def split_Arr(lst, n):
    if n > len(lst):
        return lst
    return lst[n:] + lst[:n]