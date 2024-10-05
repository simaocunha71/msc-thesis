
def exchange(lst1, lst2):
    if not lst1 or not lst2:
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            return "NO"
    for i in range(len(lst2)):
        if lst2[i] % 2 == 0:
            return "NO"
    return "YES"


