    odd_lst1 = [x for x in lst1 if x % 2 != 0]
    even_lst2 = [x for x in lst2 if x % 2 == 0]

    if len(odd_lst1) <= len(even_lst2):
        return "YES"
    else:
        return "NO"


