
def exchange(lst1, lst2):
    for i in range(len(lst2)):
        if lst2[i] % 2 != 0:
            lst2.remove(lst2[i])
    if lst1 == lst2:
        return "YES"
    else:
        return "NO"




