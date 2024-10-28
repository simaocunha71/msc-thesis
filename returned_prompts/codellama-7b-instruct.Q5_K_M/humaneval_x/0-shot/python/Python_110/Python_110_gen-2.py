
def exchange(lst1, lst2):
    for i in range(len(lst2)):
        if lst2[i] % 2 != 0:
            return "NO"
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            for j in range(len(lst2)):
                if lst1[i] == lst2[j]:
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    break
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            return "NO"
    return "YES"
