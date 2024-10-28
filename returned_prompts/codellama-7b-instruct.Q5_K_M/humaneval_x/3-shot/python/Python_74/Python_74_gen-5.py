    lst1_total_chars = sum([len(i) for i in lst1])
    lst2_total_chars = sum([len(i) for i in lst2])

    if lst1_total_chars < lst2_total_chars:
        return lst1
    elif lst1_total_chars > lst2_total_chars:
        return lst2
    else:
        return lst1


