    lst1_chars = 0
    lst2_chars = 0

    for word in lst1:
        lst1_chars += len(word)

    for word in lst2:
        lst2_chars += len(word)

    if lst1_chars < lst2_chars:
        return lst1
    elif lst1_chars > lst2_chars:
        return lst2
    else:
        return lst1
