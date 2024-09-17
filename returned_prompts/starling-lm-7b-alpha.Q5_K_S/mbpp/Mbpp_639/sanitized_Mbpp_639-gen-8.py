def sample_nam(names):
    l = 0
    for i in names:
        if i[0] != 'd' and i[0].islower():
            l += len(i)
    return l