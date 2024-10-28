def is_sublist(lst, sublst):
    if not isinstance(lst, list) or not isinstance(sublst, list):
        return False
    if not sublst:
        return True
    for i in range(len(lst)):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False