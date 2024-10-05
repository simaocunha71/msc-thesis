    def total_chars(lst):
        return sum(len(word) for word in lst)

    if total_chars(lst1) < total_chars(lst2):
        return lst1
    elif total_chars(lst2) < total_chars(lst1):
        return lst2
    else:
        return lst1

