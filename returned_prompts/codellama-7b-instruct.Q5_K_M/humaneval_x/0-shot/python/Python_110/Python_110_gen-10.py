
def exchange(lst1, lst2):
    lst2 = sorted(lst2)
    lst1 = sorted(lst1)
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            if lst2[0] % 2 == 0:
                lst1[i], lst2[0] = lst2[0], lst1[i]
            else:
                return "NO"
    return "YES"