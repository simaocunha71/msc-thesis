    even_list = []
    odd_list = []
    for elem in lst1:
        if elem % 2 == 0:
            even_list.append(elem)
        else:
            odd_list.append(elem)
    for elem in lst2:
        if elem % 2 == 0:
            even_list.append(elem)
        else:
            odd_list.append(elem)
    if len(odd_list) % 2 == 0:
        return "YES"
    else:
        return "NO"


