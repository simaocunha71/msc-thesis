def consecutive_duplicates(l):
    r = []
    for i in range(len(l)):
        if i == 0 or l[i] != l[i-1]:
            r.append(l[i])
    return r