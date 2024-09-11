def is_sublist(lst1, lst2):
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    if lst1_len < lst2_len:
        return False
    for i in range(lst1_len - lst2_len + 1):
        if lst1[i:i+lst2_len] == lst2:
            return True
    return False