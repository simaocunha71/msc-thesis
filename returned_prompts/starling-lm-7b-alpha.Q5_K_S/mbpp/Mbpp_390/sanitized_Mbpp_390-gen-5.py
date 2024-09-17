def add_string(L,format):
    new_L = []
    for i in L:
        new_L.append(format.format(i))
    return new_L