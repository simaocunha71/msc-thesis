def interleave_lists(l1, l2, l3):
    return [x for i in range(len(l1)) for x in [l1[i], l2[i], l3[i]]]


interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])




"""
def interleave_lists(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        l.append(l1[i])
        l.append(l2[i])
        l.append(l3[i])
    return l

def interleave_lists(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        l.extend([l1[i], l2[i], l3[i]])
    return l
"""




"""
def interleave_lists(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        l.append(l1[i])
        l.append(l2[i])
        l.append(l3[i])
    return l

def interleave_lists(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        l.extend([l1[i], l2[i], l3[i]])
    return l
"""














































































"""
def interleave_lists(l1, l2, l3):
    return [x for i in range(len(l1)) for x in [