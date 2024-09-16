def is_sublist(list, sublist):
    if not sublist:
        return True
    if not list:
        return False
    if list[0] == sublist[0]:
        return is_sublist(list[1:], sublist[1:])
    return is_sublist(list[1:], sublist)