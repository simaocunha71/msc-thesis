def total_match(lst1, lst2):
    def total_chars(lst):
        return sum(len(word) for word in lst)
    total1 = total_chars(lst1)
    total2 = total_chars(lst2)
    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1