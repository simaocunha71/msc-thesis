def total_match(lst1, lst2):
    return lst1 if sum(len(i) for i in lst1) <= sum(len(i) for i in lst2) else lst2
B:
def total_match(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if sum(len(i) for i in lst1) < sum(len(i) for i in lst2):
                return lst1
            elif sum(len(i) for i in lst1) > sum(len(i) for i in lst2):
                return lst2
            else:
                return lst1
C:
def total_match(lst1, lst2):
    if sum(len(i) for i in lst1) <= sum(len(i) for i in lst2):
        return lst1
    else:
        return lst2
D:
def total_match(lst1, lst2):
    return lst1 if sum(len(i) for i in lst1) <= sum(len(i) for i in lst2) else lst2
E:
def total_match(lst1,lst2):
    if sum(len(i) for i in lst1) < sum(len(i) for i in lst2):
        return lst1
    else:
        return lst2
F:
def total_match(lst1, lst2):
    if sum(len(i) for i in lst1) <= sum(len(i) for i in lst2):
        return lst1
    else:
        return lst2
G:
def total_match(lst1, lst2):
    return lst1 if sum(len(i) for i in lst1) < sum(len(i) for i in lst2) else lst2
H:
def total_match(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if sum(len(i) for i in lst1) < sum(len(i) for i in lst2):
                return lst1
            elif sum(len(i) for i in lst1) > sum(len(i) for i in lst2):
                return lst2
            else:
                return lst2
I:
def total_match(lst1, lst2):
    if sum(len(i) for i in lst1) > sum(len(i) for i in lst2):
        return lst1
    else:
        return lst2
J:
def total_match(lst1, lst2):
    if sum(len(i) for i in lst1) < sum