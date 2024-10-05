    l.sort()
    for i in range(len(l)):
        target = -l[i]
        if i > 0 and l[i] == l[i-1]:
            continue
        if target in l[i+1:]:
            return True
    return False


