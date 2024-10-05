    def get_total_chars(lst):
        total_chars = 0
        for word in lst:
            total_chars += len(word)
        return total_chars

    total_chars_lst1 = get_total_chars(lst1)
    total_chars_lst2 = get_total_chars(lst2)

    if total_chars_lst1 == total_chars_lst2:
        return lst1
    elif total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2

