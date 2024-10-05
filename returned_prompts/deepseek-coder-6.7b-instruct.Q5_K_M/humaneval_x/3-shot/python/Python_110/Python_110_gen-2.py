    odd_lst1 = [n for n in lst1 if n % 2 != 0]
    even_lst2 = [n for n in lst2 if n % 2 == 0]
    if len(odd_lst1) <= len(even_lst2):
        return "YES"
    else:
        return "NO"


