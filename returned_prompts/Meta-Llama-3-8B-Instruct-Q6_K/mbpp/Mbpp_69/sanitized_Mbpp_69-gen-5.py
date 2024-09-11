def is_sublist(lst1, lst2):
    lst2_len = len(lst2)
    for i in range(len(lst1) - lst2_len + 1):
        if lst1[i:i+lst2_len] == lst2:
            return True
    return False