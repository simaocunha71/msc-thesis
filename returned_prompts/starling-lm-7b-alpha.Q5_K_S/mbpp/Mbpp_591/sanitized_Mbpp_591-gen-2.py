def swap_List(lst):
    if len(lst) < 2:
        return lst
    else:
        return lst[len(lst) - 1:] + lst[:len(lst) - 1]