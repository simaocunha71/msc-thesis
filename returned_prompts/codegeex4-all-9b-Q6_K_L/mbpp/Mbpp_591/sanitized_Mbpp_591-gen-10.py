def swap_List(lst):
    if len(lst) < 2:
        return lst
    else:
        lst[0], lst[-1] = lst[-1], lst[0]
        return lst