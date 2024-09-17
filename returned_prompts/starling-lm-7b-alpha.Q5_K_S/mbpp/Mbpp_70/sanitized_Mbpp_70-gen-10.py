def get_equal(lst):
    if len(lst) < 2:
        return True
    else:
        return len(lst[0]) == len(lst[1])