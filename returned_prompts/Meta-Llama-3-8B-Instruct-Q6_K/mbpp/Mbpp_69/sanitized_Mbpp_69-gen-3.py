def is_sublist(lst1, lst2):
    if len(lst2) > len(lst1):
        return False
    for i in range(len(lst1)):
        if lst1[i:i+len(lst2)] == lst2:
            return True
    return False