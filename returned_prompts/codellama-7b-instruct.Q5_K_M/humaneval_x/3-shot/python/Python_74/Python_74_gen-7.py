    total_chars = sum(len(word) for word in lst1)
    other_total_chars = sum(len(word) for word in lst2)
    if total_chars < other_total_chars:
        return lst1
    elif total_chars > other_total_chars:
        return lst2
    else:
        return lst1


