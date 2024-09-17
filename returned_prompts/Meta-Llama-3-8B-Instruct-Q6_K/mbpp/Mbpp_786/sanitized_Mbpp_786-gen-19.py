def right_insertion(lst, val):
    for i in range(len(lst)):
        if lst[i] >= val:
            return i
    return len(lst)