
def total_match(lst1, lst2):
    total_chars1 = 0
    total_chars2 = 0
    for i in lst1:
        total_chars1 += len(i)
    for j in lst2:
        total_chars2 += len(j)
    if total_chars1 < total_chars2:
        return lst1
    elif total_chars1 > total_chars2:
        return lst2
    else:
        return lst1



