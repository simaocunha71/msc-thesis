    odd_elements = list(filter(lambda x: x % 2 != 0, lst1))
    even_elements = list(filter(lambda x: x % 2 == 0, lst2))
    if len(odd_elements) == 0:
        return "YES"
    elif len(odd_elements) == len(even_elements):
        return "YES"
    else:
        return "NO"


