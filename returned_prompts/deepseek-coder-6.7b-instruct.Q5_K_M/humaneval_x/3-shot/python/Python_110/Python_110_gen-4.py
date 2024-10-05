    odd_lst1 = sum([x % 2 != 0 for x in lst1])
    even_lst2 = sum([x % 2 == 0 for x in lst2])
    return "YES" if odd_lst1 <= even_lst2 else "NO"


