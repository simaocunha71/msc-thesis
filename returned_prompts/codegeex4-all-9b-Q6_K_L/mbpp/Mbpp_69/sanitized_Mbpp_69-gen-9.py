def is_sublist(lst, sublst):
    if sublst == []:
        return True
    if lst == []:
        return False
    if lst[0] == sublst[0]:
        return is_sublist(lst[1:], sublst[1:])
    else:
        return is_sublist(lst[1:], sublst)