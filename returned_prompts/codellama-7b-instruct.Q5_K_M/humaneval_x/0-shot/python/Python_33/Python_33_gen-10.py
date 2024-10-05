
def sort_third(l):
    l2 = [l[i] for i in range(0, len(l), 3)]
    l2.sort()
    l3 = [l[i] for i in range(1, len(l), 3)]
    l3.sort()
    l4 = [l[i] for i in range(2, len(l), 3)]
    l4.sort()
    return l2 + l3 + l4
