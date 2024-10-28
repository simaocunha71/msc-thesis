def swap_List(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
        del lst[1:-1]
    return lst