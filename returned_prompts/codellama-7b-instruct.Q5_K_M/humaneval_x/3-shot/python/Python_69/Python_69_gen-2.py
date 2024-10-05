    for i in range(len(lst)):
        if lst[i] > 1 and lst[i] > len(lst) // lst[i]:
            return lst[i]
    return -1


