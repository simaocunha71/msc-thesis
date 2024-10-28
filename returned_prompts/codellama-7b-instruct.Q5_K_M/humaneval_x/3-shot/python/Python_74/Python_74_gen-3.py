    total_chars = 0
    for i in lst1:
        total_chars += len(i)
    for j in lst2:
        total_chars += len(j)

    if total_chars < len(lst2):
        return lst2
    elif total_chars == len(lst2):
        return lst1
    elif total_chars > len(lst2):
        return lst1


