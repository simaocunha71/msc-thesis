def swap_List(lst):
    if len(lst) < 2:
        if len(lst) == 0:
            raise ValueError("Input list is empty")
        elif len(lst) == 1:
            return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst