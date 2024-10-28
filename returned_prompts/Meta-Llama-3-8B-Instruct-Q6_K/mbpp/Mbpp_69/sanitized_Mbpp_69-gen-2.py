def is_sublist(lst, sublst):
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst)):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False