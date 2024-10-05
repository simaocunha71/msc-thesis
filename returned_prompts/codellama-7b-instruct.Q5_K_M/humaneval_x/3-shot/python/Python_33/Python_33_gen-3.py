    l_new = []
    for i in range(0, len(l), 3):
        l_new.append(l[i])
    l_new.sort()
    for i in range(1, len(l), 3):
        l_new.append(l[i])
    for i in range(2, len(l), 3):
        l_new.append(l[i])
    return l_new


