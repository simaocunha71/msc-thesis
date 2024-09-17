def right_insertion(lst, value):
    for i in range(len(lst)):
        if lst[i] >= value:
            return i
    return len(lst)