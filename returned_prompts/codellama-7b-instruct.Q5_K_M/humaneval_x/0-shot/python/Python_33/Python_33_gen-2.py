

def sort_third(l):
    l1 = []
    l2 = []
    l3 = []
    for i in range(0, len(l), 3):
        l1.append(l[i])
        l2.append(l[i+1])
        l3.append(l[i+2])
    l1.sort()
    l2.sort()
    l3.sort()
    l = l1 + l2 + l3
    return l



