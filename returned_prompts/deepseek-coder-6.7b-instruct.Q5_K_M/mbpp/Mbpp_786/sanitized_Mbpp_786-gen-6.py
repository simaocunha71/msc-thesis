def right_insertion(lst, n):
    for i in range(len(lst)):
        if n < lst[i]:
            return i
    return len(lst)