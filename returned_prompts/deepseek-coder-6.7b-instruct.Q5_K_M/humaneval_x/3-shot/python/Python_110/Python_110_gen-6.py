    odd1 = sum(i % 2 for i in lst1)
    even2 = sum(i % 2 == 0 for i in lst2)
    if odd1 <= even2:
        return "YES"
    else:
        return "NO"


