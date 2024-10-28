def is_sublist(lst1, lst2):
    if not lst2:
        return True
    for i in range(len(lst1) - len(lst2) + 1):
        if lst1[i:i+len(lst2)] == lst2:
            return True
    return False