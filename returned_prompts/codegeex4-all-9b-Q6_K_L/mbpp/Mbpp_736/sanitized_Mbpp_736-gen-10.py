def left_insertion(lst, val):
    i = 0
    while i < len(lst) and lst[i] < val:
        i += 1
    return i