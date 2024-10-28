def Find_Max(lst):
    return max(lst, key=len)  # or return max(lst, key=lambda x: len(x)) if you want to handle non-list elements