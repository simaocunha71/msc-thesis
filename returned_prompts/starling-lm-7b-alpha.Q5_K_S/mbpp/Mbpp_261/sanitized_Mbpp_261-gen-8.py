def division_elements(t1,t2):
    l1 = list(t1)
    l2 = list(t2)
    i = 0
    while i < len(l1):
        l1[i] = l1[i]/l2[i]
        i += 1
    return tuple(l1)