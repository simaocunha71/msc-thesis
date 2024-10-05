

def sort_third(l: list):
    l_sorted = sorted(l)
    l_unsorted = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_unsorted.append(l_sorted[i])
        else:
            l_unsorted.append(l[i])
    return l_unsorted
