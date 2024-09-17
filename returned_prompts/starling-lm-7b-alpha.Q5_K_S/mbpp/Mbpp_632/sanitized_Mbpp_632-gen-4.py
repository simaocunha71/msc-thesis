def move_zero(l):
    j = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[j], l[i] = l[i], l[j]
            j += 1
    return l