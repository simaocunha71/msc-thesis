
def exchange(lst1, lst2):
    lst1.sort()
    lst2.sort()
    i = 0
    while i < len(lst1) and lst1[i] % 2 == 0:
        i += 1
    if i == len(lst1):
        return "YES"
    j = 0
    while j < len(lst2) and lst2[j] % 2 == 0:
        j += 1
    if j == len(lst2):
        return "NO"
    while i < len(lst1) and j < len(lst2):
        if lst1[i] % 2 == 0 and lst2[j] % 2 == 0:
            return "YES"
        if lst1[i] % 2 == 0:
            i += 1
        elif lst2[j] % 2 == 0:
            j += 1
        else:
            return "NO"
    return "NO"
