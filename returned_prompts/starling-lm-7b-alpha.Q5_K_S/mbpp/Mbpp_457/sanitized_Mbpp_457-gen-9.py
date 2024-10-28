def Find_Min(l):
    min = len(l[0])
    for i in l:
        if len(i) < min:
            min = len(i)
    for i in l:
        if len(i) == min:
            index = l.index(i)
    return l[index]