    def total_chars(lst):
        total = 0
        for string in lst:
            total += len(string)
        return total

    total1 = total_chars(lst1)
    total2 = total_chars(lst2)

    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    else:
        return lst1

