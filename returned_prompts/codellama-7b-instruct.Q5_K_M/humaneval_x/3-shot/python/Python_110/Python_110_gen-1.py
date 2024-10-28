    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    if all(i % 2 == 0 for i in lst1):
                        return "YES"
                    else:
                        lst1[i], lst2[j] = lst2[j], lst1[i]
    return "NO"


