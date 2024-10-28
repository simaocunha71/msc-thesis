def is_sublist(lst, sublist):
    for i in range(len(lst)):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False