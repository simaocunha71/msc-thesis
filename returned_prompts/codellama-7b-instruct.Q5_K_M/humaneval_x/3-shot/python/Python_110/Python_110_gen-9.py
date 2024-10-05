    for i in range(len(lst2)):
        if lst2[i] % 2 == 0:
            lst1[i] = lst2[i]
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            return "NO"
    return "YES"


