def is_sublist(lst, sublst):
    if not isinstance(lst, list) or not isinstance(sublst, list):
        return False
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False