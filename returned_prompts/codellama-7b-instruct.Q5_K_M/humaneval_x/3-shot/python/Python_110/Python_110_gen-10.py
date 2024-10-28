    for x in lst1:
        if x % 2 == 1:
            for y in lst2:
                if y % 2 == 0:
                    lst1[lst1.index(x)] = y
                    lst2[lst2.index(y)] = x
                    return "YES"
    return "NO"


