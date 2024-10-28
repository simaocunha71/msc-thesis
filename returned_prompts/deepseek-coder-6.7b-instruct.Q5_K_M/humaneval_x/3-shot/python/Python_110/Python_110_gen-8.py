    odd_lst1 = sum(x % 2 != 0 for x in lst1)
    even_lst2 = sum(x % 2 == 0 for x in lst2)

    if odd_lst1 <= even_lst2:
        return "YES"
    else:
        return "NO"


