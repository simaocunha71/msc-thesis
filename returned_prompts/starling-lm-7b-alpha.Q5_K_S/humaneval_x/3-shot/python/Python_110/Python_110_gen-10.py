    odd_one = set(lst1) & set(lst2)
    if odd_one:
        if len(odd_one) % 2 == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "YES"


