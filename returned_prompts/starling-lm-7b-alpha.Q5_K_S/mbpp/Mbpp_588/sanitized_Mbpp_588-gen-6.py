def big_diff(lst):
    if lst == []:
        return 0
    else:
        return max(lst) - min(lst)