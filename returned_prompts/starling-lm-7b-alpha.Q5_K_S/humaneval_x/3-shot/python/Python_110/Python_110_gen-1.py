    odds = []
    evens = []

    for elem in lst1:
        if elem % 2 == 0:
            evens.append(elem)
        else:
            odds.append(elem)

    for elem in lst2:
        if elem % 2 == 0:
            evens.append(elem)
        else:
            odds.append(elem)

    if len(odds) % 2 == 0:
        return 'YES'
    else:
        return 'NO'


