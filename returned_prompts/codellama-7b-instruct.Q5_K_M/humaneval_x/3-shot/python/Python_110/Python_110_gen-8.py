    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"

    if len(lst1) == 1 and len(lst2) == 1:
        return "YES" if lst1[0] % 2 == 0 and lst2[0] % 2 == 1 else "NO"

    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            continue
        for j in range(len(lst2)):
            if lst2[j] % 2 != 1:
                continue

            lst1[i], lst2[j] = lst2[j], lst1[i]
            return "YES"

    return "NO"
