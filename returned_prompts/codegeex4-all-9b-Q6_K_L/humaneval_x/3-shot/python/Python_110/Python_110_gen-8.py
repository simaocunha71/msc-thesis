    lst1_even = [x for x in lst1 if x % 2 == 0]
    lst2_odd = [x for x in lst2 if x % 2 == 1]

    if len(lst1_even) + len(lst2_odd) == len(lst1):
        return "YES"
    else:
        return "NO"

