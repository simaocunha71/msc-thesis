    lst1_even_count = len([x for x in lst1 if x % 2 == 0])
    lst2_odd_count = len([x for x in lst2 if x % 2 != 0])

    if lst1_even_count == len(lst1) or lst2_odd_count == len(lst2):
        return "YES"
    else:
        return "NO"