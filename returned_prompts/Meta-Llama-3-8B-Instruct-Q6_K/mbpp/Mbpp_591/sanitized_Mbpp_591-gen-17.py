def swap_List(lst):
    if len(lst) > 1:
        lst_copy = lst.copy()
        lst_copy[0], lst_copy[-1] = lst_copy[-1], lst_copy[0]
    return lst_copy