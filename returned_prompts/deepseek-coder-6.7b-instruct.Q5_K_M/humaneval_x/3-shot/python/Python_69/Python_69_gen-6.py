    for num in sorted(lst, reverse=True):
        if num >= lst.count(num):
            return num
    return -1


