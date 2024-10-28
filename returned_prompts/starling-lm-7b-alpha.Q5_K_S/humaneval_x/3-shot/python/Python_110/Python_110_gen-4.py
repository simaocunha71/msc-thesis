    odd_num = []
    even_num = []

    for i in lst1:
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)

    for i in lst2:
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)

    if len(odd_num) > 0:
        return "NO"
    else:
        return "YES"


