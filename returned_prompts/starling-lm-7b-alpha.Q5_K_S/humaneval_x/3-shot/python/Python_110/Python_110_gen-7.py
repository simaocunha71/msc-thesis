    def exchange(lst1, lst2):
        if len(lst1) != len(lst2):
            return "NO"
        for i in range(len(lst1)):
            if lst1[i] % 2 == 0:
                continue
            if lst2[i] % 2 == 0:
                lst1[i] = lst2[i]
                continue
            if i + 1 < len(lst2):
                lst1[i] = lst2[i + 1]
                lst2[i + 1] = lst2[i]
            else:
                return "NO"
        return "YES"

    return exchange(lst1, lst2)


