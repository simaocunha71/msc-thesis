
def sort_even(l):
    l2 = [l[i] for i in range(0, len(l), 2)]
    l2.sort()
    l3 = [l[i] for i in range(1, len(l), 2)]
    return l3 + l2
