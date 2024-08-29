def last(lst, target):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == target:
            return i
    return -1