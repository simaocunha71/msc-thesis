def find_dissimilar(t1, t2):
    dissimilar = []
    for i in t1:
        if i not in t2:
            dissimilar.append(i)
    for i in t2:
        if i not in t1:
            dissimilar.append(i)
    return tuple(sorted(dissimilar))